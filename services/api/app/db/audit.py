import hashlib
import json
from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.db.models import AuditEvent

ZERO_HASH = "0" * 64


def _utc_iso(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat()


def _canonical_event(payload: dict) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def append_audit_event(
    db: Session,
    *,
    tenant_id: str,
    actor_sub: str,
    action: str,
    resource_type: str,
    resource_id: str | None,
    outcome: str,
    correlation_id: str,
) -> AuditEvent:
    # Serialize per-tenant hash-chain appends on PostgreSQL to avoid concurrent forks.
    if db.get_bind().dialect.name == "postgresql":
        db.execute(
            text("SELECT pg_advisory_xact_lock(hashtextextended(:tenant_id, 0))"),
            {"tenant_id": tenant_id},
        )

    previous = db.scalar(
        select(AuditEvent)
        .where(AuditEvent.tenant_id == tenant_id)
        .order_by(AuditEvent.occurred_at.desc(), AuditEvent.id.desc())
        .limit(1)
    )
    previous_hash = previous.event_hash if previous else ZERO_HASH
    event_id = str(uuid4())
    occurred_at = datetime.now(timezone.utc)
    payload = {
        "id": event_id,
        "tenant_id": tenant_id,
        "actor_sub": actor_sub,
        "action": action,
        "resource_type": resource_type,
        "resource_id": resource_id,
        "outcome": outcome,
        "correlation_id": correlation_id,
        "occurred_at": _utc_iso(occurred_at),
        "previous_hash": previous_hash,
        "metadata": {},
    }
    event_hash = hashlib.sha256(_canonical_event(payload)).hexdigest()
    row = AuditEvent(
        id=event_id,
        tenant_id=tenant_id,
        actor_sub=actor_sub,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        outcome=outcome,
        correlation_id=correlation_id,
        occurred_at=occurred_at,
        previous_hash=previous_hash,
        event_hash=event_hash,
        metadata_json={},
    )
    db.add(row)
    db.flush()
    return row


def verify_audit_chain(events: list[AuditEvent]) -> bool:
    """Verify an ordered list of events. This detects changes; it is not tamper-proof storage."""
    previous_hash = ZERO_HASH
    for row in events:
        payload = {
            "id": row.id,
            "tenant_id": row.tenant_id,
            "actor_sub": row.actor_sub,
            "action": row.action,
            "resource_type": row.resource_type,
            "resource_id": row.resource_id,
            "outcome": row.outcome,
            "correlation_id": row.correlation_id,
            "occurred_at": _utc_iso(row.occurred_at),
            "previous_hash": previous_hash,
            "metadata": row.metadata_json or {},
        }
        calculated = hashlib.sha256(_canonical_event(payload)).hexdigest()
        if row.previous_hash != previous_hash or row.event_hash != calculated:
            return False
        previous_hash = row.event_hash
    return True

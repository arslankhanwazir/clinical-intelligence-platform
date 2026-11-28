from uuid import uuid4

from fastapi.testclient import TestClient

import app.main as main_module


def test_api_rate_limit_returns_429(monkeypatch):
    # Use a unique synthetic client address so this test is independent of prior test runs.
    client_host = f"2001:db8::{uuid4().hex[:12]}"
    monkeypatch.setattr(main_module.settings, "api_rate_limit_requests_per_minute", 2)
    monkeypatch.setattr(main_module.settings, "api_rate_limit_window_seconds", 60)

    with TestClient(main_module.app, client=(client_host, 54321)) as test_client:
        first = test_client.get("/api/v1/security/me")
        second = test_client.get("/api/v1/security/me")
        third = test_client.get("/api/v1/security/me")

    assert first.status_code == 401
    assert second.status_code == 401
    assert third.status_code == 429
    assert third.headers.get("retry-after")
    assert third.headers.get("ratelimit-limit") == "2"


def test_expired_rate_limit_buckets_are_pruned_across_clients():
    from time import time

    from sqlalchemy import text

    from app.core.rate_limit import client_key_hash, increment_request_count
    from app.db.session import engine

    now = int(time())
    window_seconds = 60
    stale_client = f"198.51.100.{uuid4().int % 250 + 1}"
    active_client = f"203.0.113.{uuid4().int % 250 + 1}"
    stale_hash = client_key_hash(stale_client)

    increment_request_count(
        engine, client_host=stale_client, now=now - (2 * window_seconds),
        window_seconds=window_seconds,
    )
    increment_request_count(
        engine, client_host=active_client, now=now, window_seconds=window_seconds,
    )

    with engine.connect() as connection:
        stale_count = connection.execute(
            text("SELECT count(*) FROM api_rate_limit_buckets WHERE key_hash = :key_hash"),
            {"key_hash": stale_hash},
        ).scalar_one()

    assert stale_count == 0

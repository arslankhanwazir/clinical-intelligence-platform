from hashlib import sha256

from sqlalchemy import text
from sqlalchemy.engine import Engine


INCREMENT_SQL = text(
    """
    INSERT INTO api_rate_limit_buckets (key_hash, window_start, request_count)
    VALUES (:key_hash, :window_start, 1)
    ON CONFLICT (key_hash, window_start)
    DO UPDATE SET request_count = api_rate_limit_buckets.request_count + 1
    RETURNING request_count
    """
)

DELETE_OLD_SQL = text(
    "DELETE FROM api_rate_limit_buckets WHERE window_start < :window_start"
)


def client_key_hash(client_host: str | None) -> str:
    # Store a digest, not the caller's raw network address.
    source = f"northstar-api-client:{client_host or 'unknown'}".encode("utf-8")
    return sha256(source).hexdigest()


def increment_request_count(engine: Engine, *, client_host: str | None, now: int, window_seconds: int) -> tuple[int, int]:
    window_start = (now // window_seconds) * window_seconds
    key_hash = client_key_hash(client_host)
    with engine.begin() as connection:
        count = connection.execute(
            INCREMENT_SQL,
            {"key_hash": key_hash, "window_start": window_start},
        ).scalar_one()
        # Remove expired windows for every client; retain only the active window buckets.
        connection.execute(
            DELETE_OLD_SQL,
            {"key_hash": key_hash, "window_start": window_start},
        )
    return int(count), window_start + window_seconds

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

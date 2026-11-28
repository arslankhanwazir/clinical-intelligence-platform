from app.core.security import get_current_principal
from app.main import app


def test_protected_endpoint_rejects_missing_bearer_token(client):
    app.dependency_overrides.pop(get_current_principal, None)
    response = client.get("/api/v1/security/me")
    assert response.status_code == 401
    assert response.headers["www-authenticate"] == "Bearer"

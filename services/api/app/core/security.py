from functools import lru_cache

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWKClient
from jwt.exceptions import PyJWKClientError, PyJWTError

from app.core.config import Settings, get_settings
from app.core.identity import Principal, principal_from_claims

bearer_scheme = HTTPBearer(auto_error=False, scheme_name="KeycloakBearer")


@lru_cache(maxsize=8)
def _jwks_client(jwks_url: str, timeout_seconds: int) -> PyJWKClient:
    return PyJWKClient(jwks_url, cache_jwk_set=True, lifespan=300, timeout=timeout_seconds)


def verify_access_token(token: str, settings: Settings) -> Principal:
    if not all((settings.oidc_issuer, settings.oidc_jwks_url, settings.oidc_audience)):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Identity provider is not configured",
        )

    try:
        client = _jwks_client(settings.oidc_jwks_url, settings.oidc_jwks_timeout_seconds)
        signing_key = client.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=settings.oidc_audience,
            issuer=settings.oidc_issuer,
            leeway=settings.jwt_leeway_seconds,
            options={"require": ["exp", "iat", "iss", "sub", "aud"]},
        )
        return principal_from_claims(claims, settings.oidc_client_id)
    except PyJWKClientError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Identity provider keys are temporarily unavailable",
        ) from exc
    except (PyJWTError, ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def get_current_principal(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    settings: Settings = Depends(get_settings),
) -> Principal:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return verify_access_token(credentials.credentials, settings)

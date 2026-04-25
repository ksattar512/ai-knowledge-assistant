from fastapi import Header, HTTPException
from app.core.config import get_settings


def validate_api_key(x_api_key: str | None = Header(default=None)) -> bool:
    """
    Simple API key validation placeholder.
    Replace with OAuth2, Microsoft Entra ID, or JWT validation in production.
    """
    settings = get_settings()

    if settings.environment == "development":
        return True

    if not x_api_key or x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    return True

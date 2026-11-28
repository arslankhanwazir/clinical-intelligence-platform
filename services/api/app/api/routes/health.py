from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db_session

router = APIRouter(tags=["health"])


@router.get("/health/live", include_in_schema=False)
def liveness():
    return {"status": "alive"}


@router.get("/health/ready", include_in_schema=False)
def readiness(db: Session = Depends(get_db_session)):
    try:
        db.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database unavailable") from exc
    return {"status": "ready", "database": "reachable"}

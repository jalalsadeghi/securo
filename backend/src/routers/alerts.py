from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.models import Alert
from sqlalchemy.future import select

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/{user_id}")
async def get_alerts(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Alert).where(Alert.user_id == user_id))
    alerts = result.scalars().all()
    return alerts

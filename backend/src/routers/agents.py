from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.models import Agent, User
from src.schemas import AgentCreate, AgentRead
from sqlalchemy.future import select

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.post("/{user_id}/create", response_model=AgentRead)
async def create_agent(user_id: int, agent: AgentCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_agent = Agent(
        user_id=user_id,
        agent_identifier=agent.agent_identifier,
        device_name=agent.device_name
    )
    db.add(new_agent)
    try:
        await db.commit()
        await db.refresh(new_agent)
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Agent identifier already exists")

    return new_agent

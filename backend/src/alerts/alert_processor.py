from .email_alert import send_alert_email
from src.models import Alert, Agent
from sqlalchemy.ext.asyncio import AsyncSession

async def process_alert(db: AsyncSession, agent_identifier: str, severity: int, alert_type: str, message: str):
    agent = await db.scalar(select(Agent).where(Agent.agent_identifier == agent_identifier))
    if not agent:
        return

    new_alert = Alert(
        user_id=agent.user_id,
        agent_id=agent.id,
        severity=severity,
        alert_type=alert_type,
        message=message
    )
    db.add(new_alert)
    await db.commit()

    if severity >= 10:
        await send_alert_email(
            email_to=agent.user.email,
            subject=f"Critical Alert: {alert_type}",
            content=message
        )

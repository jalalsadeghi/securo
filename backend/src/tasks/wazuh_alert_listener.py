import asyncio
import json
import aiofiles
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

import sys
sys.path.append("/app/src")
from src.alerts.alert_processor import process_alert
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def read_alerts():
    alerts_file = "/var/ossec/logs/alerts/alerts.json"
    last_position = 0

    while True:
        async with aiofiles.open(alerts_file, mode="r") as file:
            await file.seek(last_position)
            lines = await file.readlines()
            last_position = await file.tell()

            async with async_session() as db:
                for line in lines:
                    alert = json.loads(line)
                    await process_alert(
                        db=db,
                        agent_identifier=alert["agent"]["id"],
                        severity=int(alert["rule"]["level"]),
                        alert_type=alert["rule"]["description"],
                        message=alert["full_log"]
                    )
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(read_alerts())

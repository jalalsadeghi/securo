from fastapi import FastAPI
from src.models import Base
from src.database import engine
from src.routers import users, agents

app = FastAPI(title="Cloud Security Platform API")

app.include_router(users.router)
app.include_router(agents.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Cloud Security Backend is running!"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models import Base
from src.database import engine
from src.routers import users, agents, alerts

app = FastAPI(title="Cloud Security Platform API")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(agents.router)
app.include_router(alerts.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Cloud Security Backend is running!"}



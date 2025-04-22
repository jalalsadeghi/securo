from pydantic import BaseModel, EmailStr
from datetime import datetime

# User Schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

# Agent Schemas
class AgentCreate(BaseModel):
    agent_identifier: str
    device_name: str

class AgentRead(BaseModel):
    id: int
    agent_identifier: str
    device_name: str
    created_at: datetime

    class Config:
        from_attributes = True

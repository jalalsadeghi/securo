from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    family_name: str
    email: EmailStr
    phone_number: str
    password: str
    company: str
    country: str

class UserRead(BaseModel):
    id: int
    first_name: str
    family_name: str
    email: EmailStr
    phone_number: str
    company: str
    country: str
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

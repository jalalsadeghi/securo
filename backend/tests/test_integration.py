import pytest
import asyncio
from httpx import AsyncClient
from src.app import app
from src.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.alerts.email_alert import send_alert_email

# Fixture to provide a test database session
@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
async def user_data():
    return {"email": "testuser@example.com", "password": "StrongPass123"}

@pytest.fixture
async def agent_data():
    return {"agent_identifier": "agent123", "device_name": "TestDevice"}

# Integration test
@pytest.mark.asyncio
async def test_user_registration_and_agent_creation(async_client, user_data, agent_data):
    # Registration of a new user
    user_response = await async_client.post("/users/register", json=user_data)
    assert user_response.status_code == 200, f"Registration failed: {user_response.text}"
    user_json = user_response.json()
    assert user_json["email"] == user_data["email"]

    user_id = user_json["id"]

    # Add new user to the database
    agent_response = await async_client.post(f"/agents/{user_id}/create", json=agent_data)
    assert agent_response.status_code == 200, f"Agent creation failed: {agent_response.text}"
    agent_json = agent_response.json()
    assert agent_json["agent_identifier"] == agent_data["agent_identifier"]

    # Alert email sending
    try:
        await send_alert_email(
            email_to=user_data["email"],
            subject="Test Alert",
            content=f"Agent {agent_data['agent_identifier']} successfully registered."
        )
    except Exception as e:
        pytest.fail(f"Sending email failed: {str(e)}")

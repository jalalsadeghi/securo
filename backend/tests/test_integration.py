import pytest
from httpx import AsyncClient
from src.app import app
from src.database import get_db
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.models import Base

DATABASE_TEST_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(DATABASE_TEST_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture(scope="session")
async def async_session(engine):
    session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with session_maker() as session:
        yield session

@pytest.fixture(scope="session")
async def client(async_session):
    async def override_get_db():
        yield async_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
        app.dependency_overrides[get_db] = get_db

@pytest.mark.asyncio
async def test_user_registration(client):
    payload = {"email": "test@example.com", "password": "StrongPass123"}
    response = await client.post("/users/register", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["email"] == payload["email"]
    assert "password_hash" not in data
    assert "created_at" in data

# @pytest.mark.asyncio
# async def test_agent_creation(client):
#     user_payload = {"email": "agenttest@example.com", "password": "StrongPass123"}
#     user_response = await client.post("/users/register", json=user_payload)
#     user_id = user_response.json()["id"]

#     agent_payload = {"agent_identifier": "agent001", "device_name": "TestDevice"}
#     response = await client.post(f"/agents/{user_id}/create", json=agent_payload)
#     assert response.status_code == 200
#     agent_data = response.json()
#     assert agent_data["agent_identifier"] == agent_payload["agent_identifier"]

# @pytest.mark.asyncio
# async def test_email_alert(client, monkeypatch):
#     async def mock_send_email(*args, **kwargs):
#         return True

#     from src.alerts import email_alert
#     monkeypatch.setattr(email_alert, "send_alert_email", mock_send_email)

#     response = await client.post("/alerts/send-test-email", json={"email_to": "alerttest@example.com"})
#     assert response.status_code == 200
#     assert response.json()["message"] == "Email sent successfully"

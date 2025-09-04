import asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app


# Тестовая база данных (лучше использовать отдельную БД для тестов)
TEST_DATABASE_URL = "postgresql+asyncpg://user:password@localhost/test_db"

# Асинхронный движок для тестов
engine = create_async_engine(TEST_DATABASE_URL, echo=True)
AsyncTestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="session")
def event_loop():
    """Создает экземпляр цикла событий для тестов."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function", autouse=True)
async def setup_database():
    """Создает и очищает базу данных перед каждым тестом."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def db_session(setup_database):
    """Создает асинхронную сессию для работы с базой данных."""
    async with AsyncTestingSessionLocal() as session:
        yield session
        await session.rollback()  # Откатываем транзакцию после каждого теста

@pytest.fixture
def override_get_db(db_session):
    """Переопределяем зависимость get_db для тестов."""
    async def _override_get_db():
        yield db_session
    return _override_get_db

@pytest.fixture
async def async_client(override_get_db):
    """Создает асинхронного клиента для тестирования API."""
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()

# @pytest.fixture
# async def auth_headers(async_client):
#     """Фикстура для получения аутентификационных заголовков."""
#     # Здесь должна быть реализация получения JWT токена
#     login_data = {"username": "testuser", "password": "testpass"}
#     response = await async_client.post("/api/token", data=login_data)
#     token = response.json()["access_token"]
#     return {"Authorization": f"Bearer {token}"}
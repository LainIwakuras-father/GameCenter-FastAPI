import pytest
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import (
    get_station_service,
    get_player_team_service,
    get_auth_service,
    get_db_session
)
from app.services import StationService, PlayerTeamService, AuthService

@pytest.mark.asyncio
async def test_get_station_service():
    """Тест получения сервиса станций"""
    async for db in get_db_session():
        service = await get_station_service(db)
        assert isinstance(service, StationService)

@pytest.mark.asyncio
async def test_get_player_team_service():
    """Тест получения сервиса команд игроков"""
    async for db in get_db_session():
        service = await get_player_team_service(db)
        assert isinstance(service, PlayerTeamService)

@pytest.mark.asyncio
async def test_get_auth_service():
    """Тест получения сервиса аутентификации"""
    async for db in get_db_session():
        service = await get_auth_service(db)
        assert isinstance(service, AuthService)

@pytest.mark.asyncio
async def test_service_dependency_injection():
    """Тест инъекции зависимостей в роуты"""
    from app.api.station_routes import get_all_stations
    
    # Мок сервиса
    class MockStationService:
        async def get_all_stations(self, db, skip, limit):
            return []
    
    # Тест вызова с инъекцией зависимости
    async with get_db_session() as db:
        result = await get_all_stations(
            skip=0,
            limit=100,
            station_service=MockStationService(),
            db=db
        )
        assert result == []
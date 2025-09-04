import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curator import Curator
from app.models.player_team import PlayerTeam
from app.models.station import Station

@pytest.mark.asyncio
async def test_create_curator(db_session: AsyncSession):
    """Тест создания куратора в базе данных."""
    curator = Curator(name="Test Curator", email="test@example.com")
    db_session.add(curator)
    await db_session.commit()
    await db_session.refresh(curator)
    
    assert curator.id is not None
    assert curator.name == "Test Curator"
    assert curator.email == "test@example.com"

@pytest.mark.asyncio
async def test_create_player_team(db_session: AsyncSession):
    """Тест создания команды игроков в базе данных."""
    team = PlayerTeam(name="Test Team", score=0, current_station_id=1)
    db_session.add(team)
    await db_session.commit()
    await db_session.refresh(team)
    
    assert team.id is not None
    assert team.name == "Test Team"
    assert team.score == 0

# Добавьте аналогичные тесты для других моделей
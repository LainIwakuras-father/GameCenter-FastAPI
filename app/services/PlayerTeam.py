from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app import schemas
from app.repositories.player_team_repository import PlayerTeamRepository
from app.services.base_service import BaseService

class PlayerTeamService(BaseService):
    def __init__(self):
        super().__init__(PlayerTeamRepository())
    
    async def add_score(self, db: AsyncSession, team_id: int, score_to_add: int) -> Optional[schemas.PlayerTeam]:
        """Добавить очки команде"""
        team = await self.repository.add_score(db, team_id, score_to_add)
        if team:
            return schemas.PlayerTeam.model_validate(team)
        return None
    
    async def get_top_teams(self, db: AsyncSession, limit: int = 3) -> List[schemas.PlayerTeam]:
        """Получить топ команд по очкам"""
        teams = await self.repository.get_top_teams(db, limit)
        return [schemas.PlayerTeam.model_validate(team) for team in teams]
    
    async def set_current_station(self, db: AsyncSession, team_id: int, station_number: int) -> Optional[schemas.PlayerTeam]:
        """Установить текущую станцию для команды"""
        team = await self.repository.set_current_station(db, team_id, station_number)
        if team:
            return schemas.PlayerTeam.model_validate(team)
        return None
    
    async def get_team_with_user(self, db: AsyncSession, team_id: int) -> Optional[schemas.PlayerTeamWithUser]:
        """Получить команду с информацией о пользователе"""
        team = await self.repository.get_with_user(db, team_id)
        if team:
            return schemas.PlayerTeamWithUser.model_validate(team)
        return None
    
    async def start_game(self, db: AsyncSession, team_id: int) -> Optional[schemas.PlayerTeam]:
        """Начать игру для команды (установить время начала)"""
        from datetime import datetime
        team = await self.repository.update(db, team_id, {"start_time": datetime.now()})
        if team:
            return schemas.PlayerTeam.model_validate(team)
        return None
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from typing import List, Optional
from app.models import PlayerTeam
from app.repositories.base_repository import BaseRepository

class PlayerTeamRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayerTeam)
    
    async def get_with_user(self, db: AsyncSession, team_id: int) -> Optional[PlayerTeam]:
        result = await db.execute(
            select(PlayerTeam)
            .where(PlayerTeam.id == team_id)
            .options(selectinload(PlayerTeam.user))
        )
        return result.scalar_one_or_none()
    
    async def get_by_teamname(self, db: AsyncSession, teamname: str) -> Optional[PlayerTeam]:
        result = await db.execute(
            select(PlayerTeam)
            .where(PlayerTeam.teamname == teamname)
        )
        return result.scalar_one_or_none()
    
    async def add_score(self, db: AsyncSession, team_id: int, score_to_add: int) -> Optional[PlayerTeam]:
        result = await db.execute(select(PlayerTeam).where(PlayerTeam.id == team_id))
        team = result.scalar_one_or_none()
        if team:
            team.score = (team.score or 0) + score_to_add
            await db.commit()
            await db.refresh(team)
        return team
    
    async def get_top_teams(self, db: AsyncSession, limit: int = 3) -> List[PlayerTeam]:
        result = await db.execute(
            select(PlayerTeam)
            .order_by(PlayerTeam.score.desc())
            .limit(limit)
            .options(selectinload(PlayerTeam.user))
        )
        return result.scalars().all()
    
    async def set_current_station(self, db: AsyncSession, team_id: int, station_number: int) -> Optional[PlayerTeam]:
        return await self.update(db, team_id, {"current_station": station_number})
    
    async def get_teams_by_user_id(self, db: AsyncSession, user_id: int) -> List[PlayerTeam]:
        result = await db.execute(
            select(PlayerTeam)
            .where(PlayerTeam.user_id == user_id)
        )
        return result.scalars().all()
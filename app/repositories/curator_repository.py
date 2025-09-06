from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from sqlalchemy.orm import selectinload

from app.models.curator import Curator
from app.repositories.base_repository import SQLAlchemyRepository

class CuratorRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__()
    
    async def get_with_user(self, db: AsyncSession, curator_id: int) -> Optional[Curator]:
        result = await db.execute(
            select(Curator)
            .where(Curator.id == curator_id)
            .options(selectinload(Curator.user))
        )
        return result.scalar_one_or_none()
    
    async def get_by_station(self, db: AsyncSession, station_id: int) -> List[Curator]:
        result = await db.execute(
            select(Curator)
            .where(Curator.station_id == station_id)
            .options(selectinload(Curator.user))
        )
        return result.scalars().all()
    
    async def get_by_user_id(self, db: AsyncSession, user_id: int) -> Optional[Curator]:
        result = await db.execute(
            select(Curator)
            .where(Curator.user_id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_with_station(self, db: AsyncSession, curator_id: int) -> Optional[Curator]:
        result = await db.execute(
            select(Curator)
            .where(Curator.id == curator_id)
            .options(selectinload(Curator.station))
        )
        return result.scalar_one_or_none()
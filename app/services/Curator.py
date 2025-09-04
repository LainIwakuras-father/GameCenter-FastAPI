from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app import schemas
from app.repositories.curator_repository import CuratorRepository
from app.services.base_service import BaseService

class CuratorService(BaseService):
    def __init__(self):
        super().__init__(CuratorRepository())
    
    async def get_curator_with_user(self, db: AsyncSession, curator_id: int) -> Optional[schemas.CuratorWithUser]:
        """Получить куратора с информацией о пользователе"""
        curator = await self.repository.get_with_user(db, curator_id)
        if curator:
            return schemas.CuratorWithUser.model_validate(curator)
        return None
    
    async def get_curators_by_station(self, db: AsyncSession, station_id: int) -> List[schemas.Curator]:
        """Получить кураторов по станции"""
        curators = await self.repository.get_by_station(db, station_id)
        return [schemas.Curator.model_validate(curator) for curator in curators]
    
    async def assign_to_station(self, db: AsyncSession, curator_id: int, station_id: int) -> Optional[schemas.Curator]:
        """Назначить куратора на станцию"""
        curator = await self.repository.update(db, curator_id, {"station_id": station_id})
        if curator:
            return schemas.Curator.model_validate(curator)
        return None
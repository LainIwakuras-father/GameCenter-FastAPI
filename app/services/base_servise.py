from typing import Type, TypeVar, Optional, List, Any
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)

class BaseService:
    def __init__(self, repository: Any):
        self.repository = repository
    
    async def get_all(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[T]:
        return await self.repository.get_all(db, skip=skip, limit=limit)
    
    async def get_by_id(self, db: AsyncSession, id: int) -> Optional[T]:
        return await self.repository.get_by_id(db, id)
    
    async def create(self, db: AsyncSession, obj_in: CreateSchema) -> T:
        return await self.repository.create(db, obj_in)
    
    async def update(self, db: AsyncSession, id: int, obj_in: UpdateSchema) -> Optional[T]:
        return await self.repository.update(db, id, obj_in)
    
    async def delete(self, db: AsyncSession, id: int) -> bool:
        return await self.repository.delete(db, id)
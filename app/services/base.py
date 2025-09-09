from typing import TypeVar, Generic, List, Optional, Type, Any
from pydantic import BaseModel

from app.repositories.base import AbstractRepository


T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)

class BaseService(Generic[T, CreateSchema, UpdateSchema]):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository
    
    async def get_all(self, **filters) -> List[T]:
        return await self.repository.get_all(**filters)
    
    async def get_by_id(self, id: int) -> Optional[T]:
        return await self.repository.get_by_id(id)
    
    async def create(self, data: dict) -> T:
        return await self.repository.create(data)
    
    async def update(self, id: int, data: dict) -> Optional[T]:
        return await self.repository.update(id, data)
    
    async def delete(self, **filters) -> bool:
        return await self.repository.delete(**filters)
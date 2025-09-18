from abc import ABC, abstractmethod
from typing import List, Optional, Type, TypeVar

from tortoise import Model


class AbstractRepository(ABC):
    # Абстрактный азовый класс для всех  репозиториев
    @abstractmethod
    async def create(self, data):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id, data):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **filter_by):
        raise NotImplementedError


ModelType = TypeVar("ModelType", bound=Model)


class BaseRepository(AbstractRepository):
    """Базовая реализация репозитория для работы с моделями Tortoise ORM"""

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(self) -> List[ModelType]:
        return await self.model.all()

    async def get_by_id(self, id: int) -> Optional[ModelType]:
        return await self.model.get_or_none(id=id)

    async def create(self, **kwargs) -> ModelType:
        return await self.model.create(**kwargs)

    async def update(self, id: int, **kwargs) -> Optional[ModelType]:
        instance = await self.model.get_or_none(id=id)
        if instance:
            await instance.update_from_dict(kwargs).save()
            return instance
        return None

    async def delete(self, id: int) -> bool:
        instance = await self.model.get_or_none(id=id)
        if instance:
            await instance.delete()
            return True
        return False

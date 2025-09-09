from typing import Any, Dict, List, Optional
from app.models.curator import Curator
from app.models.user import User
from app.repositories.base import BaseRepository


class CuratorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Curator)

    async def get_all(self) -> List[Curator]:
        return await Curator.all().prefetch_related("user", "station").all()

    async def get_by_id(self, id: int) -> Optional[Curator]:
        return await Curator.filter(id=id).prefetch_related("user", "station").first()

    async def create(self, user_data: Dict[str, Any], curator_data: Dict[str, Any]) -> Curator:
        user = await User.create(**user_data)
        curator_data["user_id"] = user.id
        return await self.create(curator_data) 
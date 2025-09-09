from typing import List, Optional, Dict, Any
from app.repositories.curator import CuratorRepository


class CuratorService():
    repository = CuratorRepository()
    
    async def get_all_curators(self) -> List[Any]:
        return await self.repository.get_all()
    
    async def get_curator_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_curator(self, curator_data: Dict[str, Any]) -> Any:
        return await self.repository.create(curator_data)
    
    async def update_curator(self, id: int, curator_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, curator_data)
    
    async def delete_curator(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    

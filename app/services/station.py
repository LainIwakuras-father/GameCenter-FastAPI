from typing import List, Optional, Dict, Any
from app.services.base import BaseService
from app.repositories.station import StationRepository

class StationService(BaseService):
    def __init__(self, repository: StationRepository = None):
        super().__init__(repository or StationRepository())
    
    async def get_all_stations(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return await self.repository.get_all(skip=skip, limit=limit)
    
    async def get_station_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_station(self, station_data: Dict[str, Any]) -> Any:
        return await self.repository.create(station_data)
    
    async def update_station(self, id: int, station_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, station_data)
    
    async def delete_station(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    

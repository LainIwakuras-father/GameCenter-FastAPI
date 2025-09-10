from typing import List, Optional, Dict, Any

from app.repositories.station import StationRepository

class StationService():
    repository = StationRepository()
    
    async def get_all_stations(self) -> List[Any]:
        return await self.repository.get_all_with_tasks()
    
    async def get_station_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_station(self, station_data: Dict[str, Any]) -> Any:
        return await self.repository.create(**station_data)
    
    async def update_station(self, id: int, station_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, station_data)
    
    async def delete_station(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    

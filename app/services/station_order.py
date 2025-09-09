from typing import List, Optional, Dict, Any
from app.services.base import BaseService
from app.repositories.station_order import StationOrderRepository

class StationOrderService(BaseService):
    def __init__(self, repository: StationOrderRepository = None):
        super().__init__(repository or StationOrderRepository())
    
    async def get_all_station_orders(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return await self.repository.get_all_with_relations(skip=skip, limit=limit)
    
    async def get_station_order_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id_with_relations(id)
    
    async def create_station_order(self, order_data: Dict[str, Any]) -> Any:
        return await self.repository.create(order_data)
    
    async def update_station_order(self, id: int, order_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, order_data)
    
    async def delete_station_order(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    
    async def get_station_orders_by_station(self, station_id: int) -> List[Any]:
        return await self.repository.get_station_orders_by_station(station_id)
    
    async def update_station_in_order(self, id: int, position: str, station_id: int) -> Optional[Any]:
        return await self.repository.update_station_in_order(id, position, station_id)
    
    async def get_complete_route(self, id: int) -> List[Any]:
        return await self.repository.get_complete_route(id)
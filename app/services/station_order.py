from typing import List, Optional, Dict, Any

from repositories.station_order import StationOrderRepository

class StationOrderService():
    repository = StationOrderRepository()
    
    async def get_all_station_orders(self) -> List[Any]:
        return await self.repository.get_all()
    
    async def get_station_order_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_station_order(self, order_data: Dict[str, Any]) -> Any:
        return await self.repository.create(**order_data)
    
    async def update_station_order(self, id: int, order_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, **order_data)
    
    async def delete_station_order(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    
    # async def get_station_orders_by_station(self, station_id: int) -> List[Any]:
    #     return await self.repository.get_station_orders_by_station(station_id)
    
    # async def update_station_in_order(self, id: int, position: str, station_id: int) -> Optional[Any]:
    #     return await self.repository.update_station_in_order(id, position, station_id)
    
    # async def get_complete_route(self, id: int) -> List[Any]:
    #     return await self.repository.get_complete_route(id)
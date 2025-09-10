from tortoise.expressions import Q
from typing import Any, Dict, List, Optional
from app.models.station import Station
from app.models.station_order import StationOrder
from app.repositories.base import BaseRepository


class StationOrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(StationOrder)


    # async def get_all_with_relations(self, skip: int = 0, limit: int = 100) -> List[StationOrder]:
    #     """Получить все записи StationOrder с загруженными связанными станциями"""
    #     return await StationOrder.all().prefetch_related(
    #         "first", "second", "third", "fourth", "fifth"
    #     ).all()

    # async def get_by_id_with_relations(self, id: int) -> Optional[StationOrder]:
    #     """Получить StationOrder по ID с загруженными связанными станциями"""
    #     return await StationOrder.filter(id=id).prefetch_related(
    #         "first", "second", "third", "fourth", "fifth",
    #         "sixth", "seventh", "eighth", "ninth", "tenth"
    #     ).first()

    # async def get_station_orders_by_station(self, station_id: int) -> List[StationOrder]:
    #     """Найти все StationOrder, где станция присутствует в любом из полей"""
    #     return await StationOrder.filter(
    #         Q(first_id=station_id) | Q(second_id=station_id) | 
    #         Q(third_id=station_id) | Q(fourth_id=station_id) | 
    #         Q(fifth_id=station_id) | Q(sixth_id=station_id) | 
    #         Q(seventh_id=station_id) | Q(eighth_id=station_id) | 
    #         Q(ninth_id=station_id) | Q(tenth_id=station_id)
    #     ).prefetch_related(
    #         "first", "second", "third", "fourth", "fifth",
    #         "sixth", "seventh", "eighth", "ninth", "tenth"
    #     ).all()

    # async def create_with_stations(self, station_data: Dict[str, Any]) -> StationOrder:
    #     """Создать StationOrder с указанием станций для всех позиций"""
    #     return await self.create(station_data)

    # async def update_station_in_order(self, id: int, position: str, station_id: int) -> Optional[StationOrder]:
    #     """Обновить конкретную позицию в StationOrder"""
    #     update_data = {position: station_id}
    #     return await self.update(id, update_data)

    # async def get_complete_route(self, id: int) -> List[Optional[Station]]:
    #     """Получить полный маршрут в виде упорядоченного списка станций"""
    #     station_order = await self.get_by_id_with_relations(id)
    #     if not station_order:
    #         return []
        
    #     # Собираем все станции в правильном порядке
    #     stations = [
    #         station_order.first, station_order.second, station_order.third,
    #         station_order.fourth, station_order.fifth, station_order.sixth,
    #         station_order.seventh, station_order.eighth, station_order.ninth,
    #         station_order.tenth
    #     ]
        
    #     # Фильтруем None значения (не заданные станции)
    #     return [station for station in stations if station is not None]
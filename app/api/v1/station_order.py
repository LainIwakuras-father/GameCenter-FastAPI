from fastapi import APIRouter

from services.station_order import StationOrderService
from schemas.station_order import StationOrderCreate, StationOrderUpdate

router = APIRouter(tags=["stationorder"])

station_order_service = StationOrderService()


@router.get("/api/stationorder")
async def get_all_station_order():
    return await station_order_service.get_all_station_orders()


@router.get("/api/stationorder/{id}")
async def get_station_order_by_id(id: int):
    return await station_order_service.get_station_order_by_id(id=id)


@router.post("/api/stationorder")
async def create_station_order(order_data: StationOrderCreate):
    return await station_order_service.create_station_order(
        order_data=order_data.model_dump()
    )


@router.put("/api/stationorder/{id}")
async def update_station_order(id: int, order_data: StationOrderUpdate):
    return await station_order_service.update_station_order(
        id=id, order_data=order_data.model_dump()
    )


@router.delete("/api/stationorder/{id}")
async def delete_station_order(id: int):
    return await station_order_service.delete_station_order(id=id)

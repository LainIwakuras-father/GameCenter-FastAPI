from fastapi import APIRouter

station_order_router = APIRouter()

@station_order_router.get("/api/stationorder")
async def get_all_station_order():
    pass

@station_order_router.get("/api/stationorder/{id}")
async def get_station_order_by_id(id: int):
    pass

@station_order_router.post("/api/stationorder")
async def create_station_order():
    pass

@station_order_router.put("/api/stationorder/{id}")
async def update_station_order(id: int):
    pass

@station_order_router.delete("/api/stationorder/{id}")
async def delete_station_order(id: int):
    pass


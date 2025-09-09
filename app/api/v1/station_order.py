from fastapi import APIRouter

router = APIRouter(tags=["stationorder"])

@router.get("/api/stationorder")
async def get_all_station_order():
    pass

@router.get("/api/stationorder/{id}")
async def get_station_order_by_id(id: int):
    pass

@router.post("/api/stationorder")
async def create_station_order():
    pass

@router.put("/api/stationorder/{id}")
async def update_station_order(id: int):
    pass

@router.delete("/api/stationorder/{id}")
async def delete_station_order(id: int):
    pass


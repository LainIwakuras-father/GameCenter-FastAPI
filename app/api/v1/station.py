from fastapi import APIRouter

station_router = APIRouter()

@station_router.get("/api/station")
async def get_all_station():
    pass

@station_router.get("/api/station/{id}")
async def get_station_by_id(id: int):
    pass

@station_router.post("/api/station")
async def create_station():
    pass

@station_router.put("/api/station/{id}")
async def update_station(id: int):
    pass

@station_router.delete("/api/station/{id}")
async def delete_station(id: int):
    pass
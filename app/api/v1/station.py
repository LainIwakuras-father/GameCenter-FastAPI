from fastapi import APIRouter

router = APIRouter()

@router.get("/api/station")
async def get_all_station():
    pass

@router.get("/api/station/{id}")
async def get_station_by_id(id: int):
    pass

@router.post("/api/station")
async def create_station():
    pass

@router.put("/api/station/{id}")
async def update_station(id: int):
    pass

@router.delete("/api/station/{id}")
async def delete_station(id: int):
    pass
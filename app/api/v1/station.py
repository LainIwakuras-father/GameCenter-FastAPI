from typing import List
from fastapi import APIRouter

from app.schemas.station import StationCreate, StationUpdate, StationWithRelations
from app.services.station import StationService

router = APIRouter(tags=["station"])

#создание экземпляра для взаимодействия с сервисом  Станций
station_service = StationService()
# ,response_model=List[StationWithRelations]
@router.get("/api/station")
async def get_all_station():
    return await station_service.get_all_stations()

@router.get("/api/station/{id}")
async def get_station_by_id(id: int):
    return await station_service.get_station_by_id(id=id)

@router.post("/api/station",response_model=StationCreate)
async def create_station(station_data:StationCreate):
    return await station_service.create_station(station_data.model_dump())

@router.put("/api/station/{id}")
async def update_station(id: int, station_data:StationUpdate):
    return await station_service.update_station(id=id,station_data=station_data.model_dump())

@router.delete("/api/station/{id}")
async def delete_station(id: int):
    return await station_service.delete_station(id)
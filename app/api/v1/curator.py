from fastapi import APIRouter, Depends, HTTPException

from schemas.curator import CuratorCreate, CuratorUpdate
from services.curator import CuratorService
from utils.dependencies import IsAuthenticated

router = APIRouter(tags=["curators"], dependencies=[Depends(IsAuthenticated)])

# создаю экземпляр для взаимодействия с сервисом куратор
curator_service = CuratorService()


@router.get("/api/curator")
async def get_all_curator():
    return await curator_service.get_all_curators()


@router.get("/api/curator/{id}")
async def get_curator_by_id(id: int):
    curator = await curator_service.get_curator_by_id(id)
    if not curator:
        raise HTTPException(status_code=404, detail="Curator not found")
    return curator


@router.post("/api/curator")
async def create_curator(curator_data: CuratorCreate):
    return await curator_service.create_curator(curator_data.model_dump())


@router.put("/api/curator/{id}")
async def update_curator(id: int, curator_data: CuratorUpdate):
    return await curator_service.update_curator(
        id=id, curator_data=curator_data.model_dump()
    )


@router.delete("/api/curator/{id}")
async def delete_curator(id: int):
    return await curator_service.delete_curator(id)

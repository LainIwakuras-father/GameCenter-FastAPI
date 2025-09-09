from fastapi import APIRouter, HTTPException

from app.schemas.curator import CuratorCreate
from app.services import curator_service

router = APIRouter(prefix="/api/curator", tags=["curators"])

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
async def update_curator(id: int):
    pass

@router.delete("/api/curator/{id}")
async def delete_curator(id: int):
    pass






from fastapi import APIRouter

router = APIRouter()

@router.get("/api/curator")
async def get_all_curator():
    pass

@router.get("/api/curator/{id}")
async def get_curator_by_id(id: int):
    pass

@router.post("/api/curator")
async def create_curator():
    pass

@router.put("/api/curator/{id}")
async def update_curator(id: int):
    pass

@router.delete("/api/curator/{id}")
async def delete_curator(id: int):
    pass






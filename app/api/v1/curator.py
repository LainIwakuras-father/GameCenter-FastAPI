from fastapi import APIRouter

curator_router = APIRouter

@curator_router.get("/api/curator")
async def get_all_curator():
    pass

@curator_router.get("/api/curator/{id}")
async def get_curator_by_id(id: int):
    pass

@curator_router.post("/api/curator")
async def create_curator():
    pass

@curator_router.put("/api/curator/{id}")
async def update_curator(id: int):
    pass

@curator_router.delete("/api/curator/{id}")
async def delete_curator(id: int):
    pass






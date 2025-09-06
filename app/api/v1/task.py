from fastapi import APIRouter

router = APIRouter()

@router.get("/api/task")
async def get_all_tasks():
    pass

@router.get("/api/task/{id}")
async def get_task_by_id(id: int):
    pass

@router.post("/api/task{id}")
async def create_task():
    pass

@router.put("/api/task{id}")
async def update_task():
    pass

@router.delete("/api/task{id}")
async def delete_task():
    pass


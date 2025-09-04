from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/api/task")
async def get_all_tasks():
    pass

@task_router.get("/api/task/{id}")
async def get_task_by_id(id: int):
    pass

@task_router.post("/api/task{id}")
async def create_task():
    pass

@task_router.put("/api/task{id}")
async def update_task():
    pass

@task_router.delete("/api/task{id}")
async def delete_task():
    pass


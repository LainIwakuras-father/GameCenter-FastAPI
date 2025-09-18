from fastapi import APIRouter

from schemas.task import TaskCreate, TaskUpdate
from services.task import TaskService


router = APIRouter(tags=["task"])

# создаю экземплер для взаимодействия с сервисом задач
task_service = TaskService()


@router.get("/api/task")
async def get_all_tasks():
    return await task_service.get_all_tasks()


@router.get("/api/task/{id}")
async def get_task_by_id(id: int):
    return await task_service.get_task_by_id(id=id)


@router.post("/api/task", response_model=TaskCreate)
async def create_task(task_data: TaskCreate):
    return await task_service.create_task(task_data.model_dump())


@router.put("/api/task{id}", response_model=TaskUpdate)
async def update_task(id: int, task_data: TaskUpdate):
    return await task_service.update_task(id=id, task_data=task_data.model_dump())


@router.delete("/api/task{id}")
async def delete_task(id: int):
    return await task_service.delete_task(id)

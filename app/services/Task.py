from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app import schemas
from app.repositories.task_repository import TaskRepository
from app.services.base_servise import BaseService


class TaskService(BaseService):
    def __init__(self):
        super().__init__(TaskRepository())
    
    async def verify_answer(self, db: AsyncSession, task_id: int, answer: str) -> bool:
        """Проверить ответ на задание"""
        task = await self.repository.get_by_id(db, task_id)
        if task and task.answer:
            return task.answer.lower().strip() == answer.lower().strip()
        return False
    
    async def get_tasks_by_name(self, db: AsyncSession, name: str) -> List[schemas.Task]:
        """Получить задания по имени"""
        tasks = await self.repository.get_by_name(db, name)
        return [schemas.Task.model_validate(task) for task in tasks]
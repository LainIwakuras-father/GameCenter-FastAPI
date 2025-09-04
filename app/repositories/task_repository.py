from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.models import Task
from app.repositories.base_repository import BaseRepository

class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(Task)
    
    async def get_by_name(self, db: AsyncSession, name: str) -> List[Task]:
        result = await db.execute(
            select(Task)
            .where(Task.name.ilike(f"%{name}%"))
        )
        return result.scalars().all()
    
    async def get_tasks_with_stations(self, db: AsyncSession) -> List[Task]:
        result = await db.execute(
            select(Task)
            .options(selectinload(Task.stations))
        )
        return result.scalars().all()
    
    async def get_by_question(self, db: AsyncSession, question: str) -> Optional[Task]:
        result = await db.execute(
            select(Task)
            .where(Task.question.ilike(f"%{question}%"))
        )
        return result.scalar_one_or_none()
from typing import List, Optional, Dict, Any
from app.services.base import BaseService
from app.repositories.task import TaskRepository

class TaskService(BaseService):
    def __init__(self, repository: TaskRepository = None):
        super().__init__(repository or TaskRepository())
    
    async def get_all_tasks(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return await self.repository.get_all_with_relations(skip=skip, limit=limit)
    
    async def get_task_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id_with_relations(id)
    
    async def create_task(self, task_data: Dict[str, Any]) -> Any:
        return await self.repository.create(task_data)
    
    async def update_task(self, id: int, task_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, task_data)
    
    async def delete_task(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    

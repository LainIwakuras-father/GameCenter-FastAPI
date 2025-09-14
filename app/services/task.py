from typing import List, Optional, Dict, Any

from repositories.task import TaskRepository

class TaskService():
    repository = TaskRepository()
    
    async def get_all_tasks(self) -> List[Any]:
        return await self.repository.get_all()
    
    async def get_task_by_id(self, id: int) -> Optional[Any]:
        return await self.repository.get_by_id(id)
    
    async def create_task(self, task_data: Dict[str, Any]) -> Any:
        return await self.repository.create(**task_data)# не забудь про звездочки
    
    async def update_task(self, id: int, task_data: Dict[str, Any]) -> Optional[Any]:
        return await self.repository.update(id, **task_data)
    
    async def delete_task(self, id: int) -> bool:
        return await self.repository.delete(id=id)
    

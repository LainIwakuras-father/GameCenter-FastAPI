from app.models.task import Task
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(Task)
from models.models import Task
from repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(Task)
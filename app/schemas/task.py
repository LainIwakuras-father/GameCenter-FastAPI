# Task schemas
from typing import Optional

from schemas.base import BaseSchema


class TaskBase(BaseSchema):
    name: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int

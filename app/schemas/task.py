# Task schemas
from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    name: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
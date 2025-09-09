# Station schemas
from datetime import timedelta
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.base import BaseSchema
from app.schemas.task import Task

class StationBase(BaseModel):
    time: Optional[timedelta] = None
    points: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    assignment: Optional[str] = None
    task_id: Optional[int] = None

class StationCreate(StationBase):
    pass

class StationUpdate(StationBase):
    pass



# Схемы с отношениями
class TaskNested(BaseSchema):
    id: int
    name: Optional[str] = None
    question: Optional[str] = None

class StationWithRelations(StationBase):
    id: int
    task: Optional[TaskNested] = None
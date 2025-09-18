# Station schemas
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from schemas.base import BaseSchema


class StationBase(BaseModel):
    time: Optional[datetime] = None
    points: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    assignment: Optional[str] = None
    task_id: Optional[int] = None


class StationCreate(BaseSchema):
    points: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    assignment: Optional[str] = None
    task_id: Optional[int] = None


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

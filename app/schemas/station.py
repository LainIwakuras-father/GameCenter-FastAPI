# Station schemas
from datetime import timedelta
from typing import Optional
from pydantic import BaseModel, ConfigDict

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

class Station(StationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)



class StationWithTask(Station):
    task: Optional[Task] = None
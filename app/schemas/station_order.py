# StationOrder schemas
from typing import Optional
from pydantic import BaseModel

from schemas.base import BaseSchema


class StationOrderBase(BaseModel):
    first_id: Optional[int] = None
    second_id: Optional[int] = None
    third_id: Optional[int] = None
    fourth_id: Optional[int] = None
    fifth_id: Optional[int] = None


class StationOrderCreate(StationOrderBase):
    pass


class StationOrderUpdate(StationOrderBase):
    pass


# Схемы с отношениями
class StationNested(BaseSchema):
    id: int
    name: str
    description: Optional[str] = None


class StationOrderWithRelations(StationOrderBase):
    id: int
    first: Optional[StationNested] = None
    second: Optional[StationNested] = None
    third: Optional[StationNested] = None
    fourth: Optional[StationNested] = None
    fifth: Optional[StationNested] = None
    sixth: Optional[StationNested] = None
    seventh: Optional[StationNested] = None
    eighth: Optional[StationNested] = None
    ninth: Optional[StationNested] = None
    tenth: Optional[StationNested] = None

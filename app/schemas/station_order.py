# StationOrder schemas
from typing import Optional
from pydantic import BaseModel, ConfigDict


class StationOrderBase(BaseModel):
    first_id: Optional[int] = None
    second_id: Optional[int] = None
    third_id: Optional[int] = None
    fourth_id: Optional[int] = None
    fifth_id: Optional[int] = None
    sixth_id: Optional[int] = None
    seventh_id: Optional[int] = None
    eighth_id: Optional[int] = None
    ninth_id: Optional[int] = None
    tenth_id: Optional[int] = None

class StationOrderCreate(StationOrderBase):
    pass

class StationOrder(StationOrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
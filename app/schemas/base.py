from pydantic import BaseModel, ConfigDict
from datetime import datetime, timedelta
from typing import Optional, List

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class BaseCreateSchema(BaseModel):
    pass

class BaseUpdateSchema(BaseModel):
    pass
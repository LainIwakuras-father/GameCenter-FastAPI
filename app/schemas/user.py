from pydantic import BaseModel, ConfigDict, EmailStr, Field



class UserLoginSchema(BaseModel):
    username: str = Field(max_length=40)
    password: str = Field(min_length=4)

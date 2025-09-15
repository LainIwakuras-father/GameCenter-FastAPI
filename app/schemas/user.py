from pydantic import BaseModel, ConfigDict, EmailStr, Field


# class UserSchema(BaseModel):
#     model_config = ConfigDict(strict=True)
#     username: str
#     password: bytes
#     email: EmailStr | None = None
#     active: bool = True


class UserLoginSchema(BaseModel):
    username: str = Field(max_length=40)
    password: str = Field(min_length=6)

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from models.user import User
from utils.auth_utils import verify_password,create_encoded_access_token
from utils.dependencies import get_current_user
from pydantic import BaseModel







class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

router = APIRouter(tags=["auth"])

@router.get("/api/token")
async def login_for_access_token(form_data:UserLogin):
    # Ищем пользователя по username
    user = await User.get_or_none(username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Создаем JWT токен
    access_token = create_encoded_access_token(
        payload={"user_id": user.id, "username": user.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/api/token/refresh")
async def refresh_token(current_user: User = Depends(get_current_user)):
    access_token = create_encoded_access_token(
        payload={"user_id": current_user.id, "username": current_user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/api/token/verify")
async def verify_token(current_user: User = Depends(get_current_user)):
     return {"message": "Токен валиден"}














"""
пытаюсь  аутентификацию и авторизацию через куки в JWTtoken 
register
login
logout
"""


# @router.post("/register", status_code=201, response_model=TaskBaseResponse)
# async def register_user(
#     user_data: UserCreateSchema, session: Session = Depends(get_db_session)
# ):
#     user = await UserService.find_user_by_name(
#         username=user_data.username, session=session
#     )
#     if user:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
#         )
#     name, role = user_data.username, user_data.role.value
#     return await UserService.create_user(name, role, session)


# @router.post("/login")
# async def login_user(
#     response: Response, username: str, session: Session = Depends(get_db_session)
# ):
#     user = await UserService.find_user_by_name(username=username, session=session)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Пользователя не существует ",
#         )
#     # "role": str(user.role)
#     access_token = create_encoded_access_token({"sub": str(user.id)})
#     response.set_cookie(key="users_access_token", value=access_token, httponly=True)
#     return {"access_token": access_token, "refresh_token": None}


# @router.get("/logout", response_model=TaskBaseResponse)
# async def logout_user(response: Response):
#     response.delete_cookie(key="users_access_token")
#     return {"message": "Пользователь успешно вышел из системы"}
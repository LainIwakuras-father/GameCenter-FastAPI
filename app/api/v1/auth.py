from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from core.auth import create_encoded_access_token, get_current_user
from core.db import get_db_session
from schemas.BaseRasponse import TaskBaseResponse, UserCreateSchema, UserSchema
from services.users import UserService

router = APIRouter()


"""
пытаюсь  аутентификацию и авторизацию через куки в JWTtoken 
register
login
logout
"""


@router.post("/register", status_code=201, response_model=TaskBaseResponse)
async def register_user(
    user_data: UserCreateSchema, session: Session = Depends(get_db_session)
):
    user = await UserService.find_user_by_name(
        username=user_data.username, session=session
    )
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
        )
    name, role = user_data.username, user_data.role.value
    return await UserService.create_user(name, role, session)


@router.post("/login")
async def login_user(
    response: Response, username: str, session: Session = Depends(get_db_session)
):
    user = await UserService.find_user_by_name(username=username, session=session)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователя не существует ",
        )
    # "role": str(user.role)
    access_token = create_encoded_access_token({"sub": str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {"access_token": access_token, "refresh_token": None}


@router.get("/logout", response_model=TaskBaseResponse)
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {"message": "Пользователь успешно вышел из системы"}




@router.get("/api/token")
async def get_token():
    pass

@router.get("/api/token/refresh")
async def refresh_token():
    pass

@router.get("/api/token/verify")
async def verify_token():
    pass
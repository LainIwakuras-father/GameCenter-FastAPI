from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, Request, status
from jwt import PyJWTError, decode, encode
from sqlalchemy.orm import Session

from core.config import SECRET_KEY
from core.db import get_db_session
from services.users import UserService
from utils.exceptions import (
    ForbiddenExcept,
    UnAuthenticatedExcept,
    handle_http_exceptions,
)


def create_encoded_access_token(
    payload: dict,
    secret_key: str = SECRET_KEY,
    algorithm: str = "HS256",
):
    to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=5)
    to_encode.update(exp=expire)

    encoded = encode(to_encode, secret_key, algorithm=algorithm)
    return encoded


def decoded_token(
    token: str | bytes, secret_key: str = SECRET_KEY, algorithm: str = "HS256"
):
    try:
        decoded = decode(token, secret_key, algorithm)
        return decoded
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен невалидный"
        )


def get_token(request: Request):
    token = request.cookies.get("users_access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден"
        )
    return token


@handle_http_exceptions
async def get_current_user(
    token: str = Depends(get_token), session: Session = Depends(get_db_session)
):
    payload = decoded_token(token)
    user_id = int(payload.get("sub"))
    user = await UserService.find_user_by_id(user_id, session)
    if not user:
        raise UnAuthenticatedExcept
    return user


async def get_current_moderator_user(current_user=Depends(get_current_user)):
    if current_user.role == "MODERATOR":
        return current_user
    raise ForbiddenExcept
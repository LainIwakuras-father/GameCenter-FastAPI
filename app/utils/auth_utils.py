from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Request, status
from jwt import PyJWTError, decode, encode

from app.core.config import get_auth_data
from app.utils.exception import NoJwtException

auth_data = get_auth_data()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_encoded_access_token(
    payload: dict,
    secret_key: str = auth_data["secret_key"],
    algorithm: str = auth_data["algorithm"],
    expires_minutes: int = 3
):
    to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update(exp=expire)

    encoded = encode(to_encode, secret_key, algorithm=algorithm)
    return encoded


def decoded_token(
    token: str | bytes,
    secret_key: str = auth_data["secret_key"],
    algorithm: str = auth_data["algorithm"]
):
    try:
        decoded = decode(token, secret_key, algorithm)
        return decoded
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен невалидный"
        )




def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)








# async def authenticate_user(email: EmailStr, password: str, session: AsyncSession):
#     user = await find_one_or_none(session, email=email)
#     if (
#         not user
#         or verifi_password(
#             plain_password=password, hashed_password=user.hashed_password
#         )
#         is False
#     ):
#         return None
#     return user












# def get_token(request: Request):
#     token = request.cookies.get("users_access_token")
#     if not token:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден"
#         )
#     return token


# @handle_http_exceptions
# async def get_current_user(
#     token: str = Depends(get_token), session: Session = Depends(get_db_session)
# ):
#     payload = decoded_token(token)
#     user_id = int(payload.get("sub"))
#     user = await UserService.find_user_by_id(user_id, session)
#     if not user:
#         raise UnAuthenticatedExcept
#     return user


# async def get_current_moderator_user(current_user=Depends(get_current_user)):
#     if current_user.role == "MODERATOR":
#         return current_user
#     raise ForbiddenExcept
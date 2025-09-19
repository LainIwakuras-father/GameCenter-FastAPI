from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from pydantic import BaseModel


from config.logging import app_logger as logger
from utils.exception import NoJwtException
from schemas.user import UserLoginSchema
from utils.dependencies import get_current_auth_user_for_refresh ,IsAuthenticated
from utils.helpers import create_access_token, create_refresh_token
from models.models import User
from utils.auth_utils import decoded_jwt, verify_password


router = APIRouter(tags=["auth"])


class TokenInfo(BaseModel):
    access: str


async def validate_auth_user(user_data: UserLoginSchema) -> User:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    if not (user := await User.get_or_none(username=user_data.username)):
        raise unauthed_exc

    if not verify_password(
        plain_password=user_data.password,
        hashed_password=user.hash_password,
    ):
        raise unauthed_exc

    return user


@router.post("/api/token",response_model=TokenInfo)
async def login_for_access_token(
    response: Response,
    user: User = Depends(validate_auth_user),
):
    try:
        access_token = create_access_token(user.username)
        refresh_token = create_refresh_token(user.username)
        logger.info("Created access and refresh token")
        response.set_cookie(
            key="users_refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=1 *24 * 60 * 60*1000,#1 day age cookie
            )
        logger.info("Set refresh token in cookie, key='users_refresh_token'")
        
        return TokenInfo(
            access=access_token,
        )
    except:

    
    

@router.post(
    "/api/token/refresh", response_model=TokenInfo, response_model_exclude_none=True
)
async def refresh_token(username=Depends(get_current_auth_user_for_refresh)):
    # отдать новый токен доступа если не истек рефреш токен
    new_access_token = create_access_token(username)
    return TokenInfo(
        access=new_access_token, 
    )



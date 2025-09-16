
from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Request, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from pydantic import BaseModel


from config.logging import app_logger as logger
from utils.exception import NoJwtException
from schemas.user import UserLoginSchema
from utils.dependencies import RefreshTokenBearer, get_current_auth_user_for_refresh, IsAuthenticated, get_user_role
from utils.helpers import ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE, TOKEN_TYPE_FIELD, create_access_token, create_refresh_token
from models.models import User
from utils.auth_utils  import decoded_jwt, verify_password


router = APIRouter(tags=["auth"])

class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"



async def validate_auth_user(
   user_data: UserLoginSchema
)->User:
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




@router.post("/api/token")
async def login_for_access_token(
    request: Request,
    user: User = Depends(validate_auth_user),
    
):
    # logger.info(request.headers)
    access_token = create_access_token(user.username)
    refresh_token = create_refresh_token(user.username)
    # return TokenInfo(
    #     access_token=access_token,
    #     refresh_token=refresh_token,
    # )
    logger.info(access_token)
    return {
        "access_token":access_token,
        "refresh_token": refresh_token
        }



@router.post("/api/token/refresh",
            response_model=TokenInfo,
            response_model_exclude_none=True
)
async def refresh_token(username = Depends(get_current_auth_user_for_refresh)):

    # отдать новый токен доступа если не истек рефреш токен
        new_access_token = create_access_token(username)
        return TokenInfo(
            access_token=new_access_token,
        )


@router.post("/api/token/verify")
async def verify_token(token:str):

    token_data = decoded_jwt(token)
    print(token_data)
    if  token is None:
            #Invalid Token
            raise NoJwtException()
     
    return { "detail": "Token is valid" }

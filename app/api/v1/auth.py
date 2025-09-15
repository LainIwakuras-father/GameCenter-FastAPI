from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Response, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError

from app.schemas.user import UserSchema
from app.utils.helpers import ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE, TOKEN_TYPE_FIELD, create_access_token, create_refresh_token
from models.user import User
from utils.auth_utils import create_encoded_token, decoded_jwt, decoded_token, verify_password
from pydantic import BaseModel, ConfigDict, EmailStr

http_bearer = HTTPBearer(auto_error=False)
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="/api/v1/auth/jwt/login/",
# )



class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"

router = APIRouter(tags=["auth"])

def get_current_token_payload(
    # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    token: str = Depends(oauth2_scheme),
) -> dict:
    # token = credentials.credentials
    try:
        payload = decoded_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
            # detail=f"invalid token error",
        )
    return payload



def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )


def get_user_by_token_sub(payload: dict) -> UserSchema:
    username: str | None = payload.get("sub")
    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(token_type: str):
    def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
    ) -> UserSchema:
        validate_token_type(payload, token_type)
        return get_user_by_token_sub(payload)

    return get_auth_user_from_token


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    def __call__(
        self,
        payload: dict = Depends(get_current_token_payload),
    ):
        validate_token_type(payload, self.token_type)
        return get_user_by_token_sub(payload)


# get_current_auth_user = UserGetterFromToken(ACCESS_TOKEN_TYPE)
get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)




async def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    if not (user := await User.get_or_none(username)):
        raise unauthed_exc

    if not verify_password(
        password=password,
        hashed_password=user.hash_password,
    ):
        raise unauthed_exc

    return user




def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    username: str | None = payload.get("sub")
    if user := User.get_or_none(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )

@router.get("/api/token",response_model=TokenInfo)
async def login_for_access_token(
    user: UserSchema = Depends(validate_auth_user)
):
    access_token = create_access_token(user)
    refresh_token =create_refresh_token(user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )






























@router.get("/api/token/refresh",
            response_model=TokenInfo,
            response_model_exclude_none=True
)
async def refresh_token(user: UserSchema = Depends(get_current_auth_user_for_refresh)):
    new_access_token = create_access_token(user)
    return TokenInfo(
        refresh_token=new_access_token,
        token_type="Bearer"
    )


@router.get("/api/token/verify")
async def verify_token(user: User = Depends(get_current_auth_user)):
     return {"message": "Токен валиден"}

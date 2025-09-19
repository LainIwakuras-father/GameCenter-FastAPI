from datetime import datetime
from fastapi import Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from config.logging import app_logger as logger
from models.models import User, Curator, PlayerTeam
from utils.auth_utils import decoded_jwt
from utils.exception import AccessTokenRequired, NoJwtException, RefreshTokenRequired


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    # использование вызова класса  как зависимость
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        """
        при вызове
        токен в заголовке декодируется(токен выданный ранее)
        проверка валидности(сверка если в базе )
        и верификация (а то что ли тот токен??)
        """
        creds = await super().__call__(request)

        token = creds.credentials

        token_data = decoded_jwt(token)
        if token is None:
            # Invalid Token
            raise NoJwtException()

        self.verify_token_data(token_data)
        # await self.expire_token(token_data)

        return token_data

    def verify_token_data(self, token_dict):
        raise NotImplementedError("Please Override this method in child classes")
    
    # #проверка срока жизни токена 
    # async def expire_token(self, token_data: dict):
    #     if token_data["exp"] < datetime.now():
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Токен истек",
    #         )


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data["type"] == "refresh":
            raise AccessTokenRequired()


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data["type"] == "access":
            raise RefreshTokenRequired()


async def get_current_auth_user_for_refresh(
    token_details: HTTPAuthorizationCredentials = Depends(RefreshTokenBearer()),
) -> User:
    try:
        expiry_timestamp = token_details["exp"]
        # Проверка на истекший токен обновления
        if datetime.fromtimestamp(expiry_timestamp) > datetime.now():
            username = token_details["sub"]
            return username
    except:
        raise NoJwtException()


async def IsAuthenticated(
    token_details: HTTPAuthorizationCredentials = Depends(AccessTokenBearer()),
) -> User:
    try:
        # Проверка на истекший токен доступа
        expiry_timestamp = token_details["exp"]
        if datetime.fromtimestamp(expiry_timestamp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Токен истек",
            )
        username = token_details["username"]

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Не найден ID пользователя в токене",
            )

        user = await User.get_or_none(username=username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Пользователь не найден",
            )
        return user
    except HTTPException:
        raise
    # except Exception:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Ошибка аутентификации"
    #     )


async def get_user_role(current_user: User = Depends(IsAuthenticated)) -> dict:
    """
    Получить профиль пользователя с информацией о ролях (куратор/игрок)
    """
    try:
        is_curator: bool = await Curator.exists(user=current_user)
        is_player_team: bool = await PlayerTeam.exists(user=current_user)
        logger.warning(is_curator)
        logger.warning(is_player_team)
        # Формируем ответ
        response_data = {
            "user_id": current_user.id,
            "is_curator": is_curator,
            "is_player": is_player_team,
            "curator_data": None,
            "player_data": None,
        }

        # Добавляем детальную информацию если есть роль
        if is_curator:
            curator = await Curator.get(user=current_user)
            response_data["curator_data"] = {
                "curator_id": curator.id,
            }

        if is_player_team:
            player_team = await PlayerTeam.get(user=current_user)
            response_data["player_data"] = {
                "team_id": player_team.id,
                "team_name": player_team.team_name,
            }

        return response_data

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        )

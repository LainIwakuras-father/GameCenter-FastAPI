from datetime import datetime
from fastapi import Depends,Request, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from models.curator import Curator
from models.player_team import PlayerTeam
from models.user import User
from utils.auth_utils import decoded_jwt
from utils.exception import AccessTokenRequired, NoJwtException, RefreshTokenRequired




# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


class TokenBearer(HTTPBearer):

    def __init__(self,auto_error=True):
        super().__init__(auto_error=auto_error)

    #использование вызова класса  как зависимость
    async def __call__(self, request: Request)-> HTTPAuthorizationCredentials:
        """
        при вызове 
        токен в заголовке декодируется(токен выданный ранее)
        проверка валидности(сверка если в базе )
        и верификация (а то что ли тот токен??)
        """
        creds = await super().__call__(request)

        token = creds.credentials

        token_data = decoded_jwt(token)
        if  token is None:
            #Invalid Token
            raise NoJwtException()
        
        self.verify_token_data(token_data)

        return token_data


    def verify_token_data(self,token_dict):
        raise NotImplementedError("Please Override this method in child classes")
        

    

class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if  token_data["type"]=="refresh":
            raise AccessTokenRequired()


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if  token_data["type"]=="access":
            raise RefreshTokenRequired()
        




async def get_current_auth_user_for_refresh(
        token_details: HTTPAuthorizationCredentials = Depends(RefreshTokenBearer())
)->User:
    try:
        expiry_timestamp = token_details["exp"]
        if datetime.fromtimestamp(expiry_timestamp) > datetime.now():
             username = token_details["sub"]
             return username
    except:
        raise NoJwtException()

async def get_current_user(
    token_details: HTTPAuthorizationCredentials = Depends(AccessTokenBearer())
)-> User:
    try:
        username = token_details["username"]




        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Не найден ID пользователя в токене"
            )
        
        user = await User.get_or_none(username=username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Пользователь не найден"
            )
        return user
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ошибка аутентификации"
        )
    





# async def get_user_role(user: User = Depends(get_current_user)):
#     # Проверяем, является ли пользователь куратором
#     curator = await Curator.get_or_none(user=user)
#     if curator:
#         return {"is_curator": True, "is_player": False}
    
#     # Проверяем, является ли пользователь игроком
#     player = await PlayerTeam.get_or_none(user=user)
#     if player:
#         return {"is_curator": False, "is_player": True}
    
#     # Если не нашли ни одну роль
#     return {"is_curator": False, "is_player": False}
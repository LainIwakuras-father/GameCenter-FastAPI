# import os
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DB_PORT: int = 5432
#     DB_NAME: str = "gamecenter"
#     DB_USER: str= "postgres"
#     DB_PASSWORD: str = "postgres"
#     DB_HOST: str = "localhost"



#     REDIS_HOST: str = "localhost"
#     REDIS_PORT: str = "6379"

#     SECRET_KEY: str = "*8n!lj)^x3zc)-pa(%k9*$!+ugk_4jzqivy8$rsvuib_p=^xk+"
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 3

#     ENVIRONMENT: str = "development"
    
#     @property
#     def REDIS_URL(self)->str:
#         return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

#     @property
#     def DB_URL(self)->str:
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

#     class Config:
#         env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

# settings = Settings()

# def get_auth_data():
#     return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}

import os
from dotenv import load_dotenv
from pathlib import Path
from fastadmin.settings import Settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
# UPLOAD_FOLDER = Path(f"uploads/images")
# UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
# Загружаем переменные окружения
load_dotenv(ENV_PATH)

class DBSettings:
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASS")
    DB_HOST: str = os.getenv("DB_HOST")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: str = os.getenv("REDIS_PORT", "6379")

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    @property
    def DB_URL(self) -> str:
        if self.ENVIRONMENT == "development":
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@db:{self.DB_PORT}/{self.DB_NAME}"




class AUTH_Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))

    @property
    def get_auth_data(self)->dict:
        
        return {
            "secret_key": self.SECRET_KEY,
            "algorithm": self.ALGORITHM
        }





#class ADMIN_Settings(Settings):
class ADMIN_Settings:
    ADMIN_USER_MODEL: str = os.getenv("ADMIN_USER_MODEL","User")
    ADMIN_USER_MODEL_USERNAME_FIELD: str = os.getenv("ADMIN_USER_MODEL_USERNAME_FIELD")
    ADMIN_SECRET_KEY: str = os.getenv("ADMIN_SECRET_KEY")




db_settings = DBSettings()
auth_settings = AUTH_Settings()
admin_settings = ADMIN_Settings()



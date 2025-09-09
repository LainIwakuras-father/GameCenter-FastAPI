import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_PORT: int = 5432
    DB_NAME: str = "gamecenter"
    DB_USER: str= "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"


    SECRET_KEY: str = "*8n!lj)^x3zc)-pa(%k9*$!+ugk_4jzqivy8$rsvuib_p=^xk+"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ENVIRONMENT: str = "development"
    
    @property
    def DB_URL(self)->str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

settings = Settings()

def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}
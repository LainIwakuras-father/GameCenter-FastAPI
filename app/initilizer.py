
import aioredis
from fastapi_admin import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from app.models.admin import Admin
login_provider = UsernamePasswordProvider(
    admin_model=Admin,
    enable_captcha=False,
    login_logo_url="https://preview.tabler.io/static/logo.svg"
)


async def init_db():
    pass

async def init_redis():
   redis = await aioredis.from_url(
       "redis://localhost",
        encoding="utf8",
        )
   return redis 

async def init_admin():
    admin_app.FastAPIAdmin(
        admin_model=Admin,

    )
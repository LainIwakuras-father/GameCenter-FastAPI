
import aioredis
from fastapi import FastAPI
from fastapi_admin import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.app import app as admin_app



from app.models.admin import Admin


login_provider=UsernamePasswordProvider(
                        admin_model=Admin,
                        enable_captcha=False,
                        login_logo_url="https://preview.tabler.io/static/logo.svg"
                        )

async def init_db():
    pass

# async def init_redis():
#    redis = await aioredis.from_url(
#        "redis://localhost",
#         encoding="utf8",
#         )
#    return redis 

async def init_admin(app: FastAPI):

    redis = await aioredis.from_url(
       "redis://localhost",
        encoding="utf8",
        )
    admin_app.configure(
        redis= redis,
        logo_url="https://preview.tabler.io/static/logo.svg",
        providers=login_provider
    )

    app.mount("/admin",admin_app)
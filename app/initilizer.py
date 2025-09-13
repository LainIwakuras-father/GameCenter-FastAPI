# Fuck off aioredis он устарел в 2023 оказывается блять
# вот как правильно сделать
# from redis import asyncio as aioredis
# from redis.asyncio.connection import ConnectionPool
import aioredis
from fastapi import FastAPI
from fastapi_admin import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.app import app as admin_app

from app.core.config import settings

from app.models.admin import Admin

async def init_db():
    pass

# login_provider=UsernamePasswordProvider(
#                         admin_model=Admin,
#                         login_logo_url="https://preview.tabler.io/static/logo.svg"
#                         )


# async def init_redis():
#    redis = await aioredis.from_url(
#        "redis://localhost",
#         encoding="utf8",
#         )
#    return redis 

'''
версия 3.10 стабильная но сука говно старое 
'''



# async def init_admin(app: FastAPI):

#     r = aioredis.from_url(
#         settings.REDIS_URL,
#         decode_responses=True,
#         encoding="utf8",
#         )
    
#     admin_app.configure(
#         redis= r,
#         logo_url="https://preview.tabler.io/static/logo.svg",
#         favicon_url="https://raw.githubusercontent.com/fastapi-admin/fastapi-admin/dev/images/favicon.png",
#         providers=login_provider
#     )

#     app.mount("/admin",admin_app)


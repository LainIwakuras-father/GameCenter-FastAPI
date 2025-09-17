import asyncio
from utils.auth_utils import get_password_hash
from db import init_db,close_db
from config.logging import app_logger as logger
from models.models import User

async def create_superuser():
    await init_db()
    hash_password = get_password_hash("admin")
    try:
        user = await User.get_or_none(username="admin")
        if not user:
            await User.create(
                username="admin",
                hash_password=hash_password,
                is_superuser=True
                ) 
            logger.info("SuperUser created! if not exist")



        
    except:
         logger.error("db connection error")
         raise
    finally:

        await close_db()

if __name__=="__main__":
        asyncio.run(create_superuser())
       
    

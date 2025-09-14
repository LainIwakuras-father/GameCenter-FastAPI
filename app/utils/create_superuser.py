import asyncio

from models.user import User


async def create_superuser():
    await User.create(
        username="admin",
        password="admin",
        is_superuser=True,
    )



if __name__=="__main__":
    try:
        asyncio.run(create_superuser)
        print("SuperUser created!")
    except Exception :
        print("DB not running :(")
        raise 

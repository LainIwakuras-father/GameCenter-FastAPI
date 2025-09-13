from app.models.user import User


async def create_superuser():
    await User.create(
        username="admin",
        password="admin",
        is_superuser=True,
    )

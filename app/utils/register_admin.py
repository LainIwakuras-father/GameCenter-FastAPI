

import uuid
from app.models.curator import Curator
from app.models.player_team import PlayerTeam
from app.models.station import Station
from app.models.station_order import StationOrder
from app.models.user import User



from fastadmin import register, TortoiseModelAdmin, WidgetType



from app.models.task import Task

# Админка для Task
@register(Task)
class TaskAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "question", "answer"]
    search_fields = ["name", "question"]
    list_filter = ["name"]


# Админка для User
@register(User)
class UserAdmin(TortoiseModelAdmin):
    # list_display = ["id", "username", "email", "is_active"]
    # search_fields = ["username", "email", "first_name", "last_name"]
    # list_filter = ["is_active", "is_superuser"]
    # exclude = ["password"]  # Скрываем пароль в админке

    list_display = ("id", "username", "is_superuser","is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser")
    search_fields = ("username",)
    formfield_overrides = {  # noqa: RUF012
        "username": (WidgetType.SlugInput, {"required": True}),
        "password": (WidgetType.PasswordInput, {"passwordModalForm": True}),
        "avatar_url": (
            WidgetType.Upload,
            {
                "required": False,
                # Disable crop image for upload field
                # "disableCropImage": True,
            },
        ),
    }

    async def authenticate(self, username: str, password: str) -> uuid.UUID | int | None:
        obj = await self.model_cls.filter(username=username, password=password, is_superuser=True).first()
        if not obj:
            return None
        return obj.id

    async def change_password(self, id: uuid.UUID | int, password: str) -> None:
        user = await self.model_cls.filter(id=id).first()
        if not user:
            return
        # direct saving password is only for tests - use hash
        user.password = password
        await user.save()

# Админка для Station
@register(Station)
class StationAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "points", "time"]
    search_fields = ["name", "description"]
    list_filter = ["points"]



# Админка для StationOrder
@register(StationOrder)
class StationOrderAdmin(TortoiseModelAdmin):
    list_display = ["id"]
    list_filter = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth", 
        "seventh",
        "eighth", 
        "ninth", 
        "tenth"
        ]
    
 #Админка для PlayerTeam
@register(PlayerTeam)
class PlayerTeamAdmin(TortoiseModelAdmin):
    list_display = ["id", "team_name", "score", "current_station"]
    search_fields = ["team_name"]
    list_filter = ["score", "current_station"]



# Админка для Curator
@register(Curator)
class CuratorAdmin(TortoiseModelAdmin):
    list_display = ["id", "name", "station"]
    search_fields = ["name"]
    list_filter = ["station"]
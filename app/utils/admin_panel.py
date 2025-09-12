from asyncio import Task
from fastapi_admin.app import FastAPIAdmin as admin_app
from fastapi_admin.app  import ModelResource,Dropdown
from fastapi_admin.widgets import filters
from fastapi_admin.widgets import inputs

from app.models.curator import Curator
from app.models.player_team import PlayerTeam
from app.models.station import Station
from app.models.station_order import StationOrder




 # Ресурс для Curator
@admin_app.register
class CuratorResource(ModelResource):
    label = "Curator"
    page_pre_title = "Curator list"
    page_title = "Curator Model"
    model=Curator,
    fields = [
        "id",
        "station"
        "user"
    ] 
    
# Ресурс для PlayerTeam
admin_app.register
class PlayerTeamResource(ModelResource):
    label = "Команды игроков"
    model = PlayerTeam
    fields = [
        "id",
        "user",
        "team_name",
        "start_time",
        "score",
        "stations",
        "current_station",
    ]
    filters = [
        
        filters.Search(name="team_name", label="Поиск по название команды", search_mode="contains"),
        inputs.Number(name="score", label="Минимальный счет")
    ]
    
    # Ресурс для Station
@admin_app.register
class StationResource(ModelResource):
    label = "Станции"
    model = Station
    fields = [
        "id",
        "time",
        "points",
        "name",
        "description",
        "image",
        "assignment",
        "task"
    ]
    
    # Ресурс для StationOrder
@admin_app.register
class StationOrderResource(ModelResource):
    label = "Станции и задачи"
    model = StationOrder
    fields = [
        "id",
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
    
@admin_app.register
class TaskResource(ModelResource):
    label = "Задачи"
    model = Task
    fields = [
        "id",
        "name",
        "question",
        "answer",
    ]




# Настройка меню
@admin_app.register()
class Content(Dropdown):
    label = "Content"
    icon = "fas fa-bars"
    resources = [
        TaskResource,
        StationOrderResource,
        StationResource,
        PlayerTeamResource,
        CuratorResource
    ]

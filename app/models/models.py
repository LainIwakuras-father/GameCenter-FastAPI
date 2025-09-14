

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator



from datetime import datetime


from models.curator import Curator
from models.player_team import PlayerTeam






class BaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True







class User(BaseModel):
    
    # Основные поля
    username = fields.CharField(max_length=150, unique=True)
    email = fields.CharField(max_length=255, unique=True, null=True)
    password = fields.CharField(max_length=128)
    
    # Личная информация
    first_name = fields.CharField(max_length=30, null=True)
    last_name = fields.CharField(max_length=150, null=True)
    
    # Статусы
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)
    

    class Meta:
        
        table = "users"
    
    def __str__(self):
        return self.username
    

class Curator(BaseModel):
    id = fields.IntField(pk=True)
    #one-to-many
    station = fields.ForeignKeyField("models.Station",null=True)

    #one-to-one 
    user = fields.OneToOneField(
        "models.User",
        related_name="curator"
        )
    
    name = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "curators"











from tortoise.validators import MinValueValidator

class PlayerTeam(BaseModel):

    #relationships one-to-one обращение к сущности пользователя 
    user = fields.OneToOneField(
        "models.User",
        related_name="player_team"
    )

    team_name = fields.CharField(max_length=100)
    start_time = fields.DatetimeField(null=True)
    score = fields.IntField(default=0, null=True)
    
    #one-to-many foreign key !
    stations = fields.ForeignKeyField("models.StationOrder",null=True)
    # поле с валидацией чтобы не было меньше 1!
    current_station = fields.IntField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        table = "player_teams"



class StationOrder(BaseModel):
    first = fields.ForeignKeyField("models.Station", related_name="first_orders", null=True)
    second = fields.ForeignKeyField("models.Station", related_name="second_orders", null=True)
    third = fields.ForeignKeyField("models.Station", related_name="third_orders", null=True)
    fourth = fields.ForeignKeyField("models.Station", related_name="fourth_orders", null=True)
    fifth = fields.ForeignKeyField("models.Station", related_name="fifth_orders", null=True)
    sixth = fields.ForeignKeyField("models.Station", related_name="sixth_orders", null=True)
    seventh = fields.ForeignKeyField("models.Station", related_name="seventh_orders", null=True)
    eighth = fields.ForeignKeyField("models.Station", related_name="eighth_orders", null=True)
    ninth = fields.ForeignKeyField("models.Station", related_name="ninth_orders", null=True)
    tenth = fields.ForeignKeyField("models.Station", related_name="tenth_orders", null=True)

    class Meta:
        table = "station_orders"




class Station(BaseModel):

    time = fields.DatetimeField(null=True)
    points = fields.IntField(null=True,default=0)
    name = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    image = fields.CharField(max_length=255,null=True)
    assignment = fields.TextField(null=True)
    
    task = fields.ForeignKeyField("models.Task",null=True)

    class Meta:
        table = "stations"




class Task(BaseModel):
    name = fields.CharField(max_length=100, null=True)
    question = fields.TextField(null=True)
    answer = fields.TextField(null=True)
    
    class Meta:
        table = "tasks"


# Pydantic схемы для User
User_Pydantic = pydantic_model_creator(User, name="User", exclude=("password",))
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
UserAuth_Pydantic = pydantic_model_creator(User, name="UserAuth", include=("id", "username", "email"))
#    username
#    first_name¶
# Optiona
# last_name¶
# Optiona
# email¶
# Optional
# password

# is_active
# is_superuser

# last_login
# date_joined

# curator 
# playerteam
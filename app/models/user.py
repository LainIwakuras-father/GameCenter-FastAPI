

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime

from models.curator import Curator
from models.player_team import PlayerTeam

class User(models.Model):
    id = fields.IntField(pk=True)
    
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
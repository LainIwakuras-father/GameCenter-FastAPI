

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime

from app.models.curator import Curator
from app.models.player_team import PlayerTeam

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
    
    # Даты
    last_login = fields.DatetimeField(null=True)
    date_joined = fields.DatetimeField(auto_now_add=True)
    #Отношения one-to-one
    # curator: fields.OneToOneRelation["Curator"]
    # player_team: fields.OneToOneRelation["PlayerTeam"]
   
    
    class Meta:
        table = "users"
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self) -> str:
        """Возвращает полное имя пользователя"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
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
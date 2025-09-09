from tortoise import models,fields
from tortoise.validators import MinValueValidator

class PlayerTeam(models.Model):
    id = fields.IntField(pk=True)
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



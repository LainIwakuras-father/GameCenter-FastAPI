from tortoise import fields,models

class Curator(models.Model):
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



from tortoise import models, fields

class Station(models.Model):
    id = fields.IntField(pk=True)
    time = fields.DatetimeField(null=True)
    points = fields.IntField(null=True,default=0)
    name = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    image = fields.CharField(max_length=255,null=True)
    assignment = fields.TextField(null=True)
    task = fields.ForeignKeyField("models.Task",null=True)





    
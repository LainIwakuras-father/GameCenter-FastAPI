from tortoise import models,fields

class StationOrder(models.Model):
    id = fields.IntField(pk=True)
    first = fields.ForeignKeyField("models.Station", related_name="first_orders", null=True)
    second = fields.ForeignKeyField("models.Station", related_name="second_orders", null=True)
    third = fields.ForeignKeyField("models.Station", related_name="third_orders", null=True)
    fourth = fields.ForeignKeyField("models.Station", related_name="fourth_orders", null=True)
    fifth = fields.ForeignKeyField("models.Station", related_name="fifth_orders", null=True)
    
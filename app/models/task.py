from tortoise import fields, models

class Task(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, null=True)
    question = fields.TextField(null=True)
    answer = fields.TextField(null=True)
    
    class Meta:
        table = "tasks"
# from tortoise import models, fields

# from app.models.user import User

# class Admin(models.Model):
#     id = fields.IntField(pk=True)
#     # username = fields.CharField(max_length=255, unique=True)
#     # password = fields.CharField(max_length=255)
#     user = fields.OneToOneField(
#         "models.User",
#         related_name="admin"
#     )





#     is_superuser = fields.BooleanField(default=False)
    
#     class Meta:
#         table = "admins"
    
#     def __str__(self):
#         return self.username
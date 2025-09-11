

class Admin(models.Model):
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    is_superuser = fields.BooleanField(default=False)
    
    class Meta:
        table = "admins"
    
    def __str__(self):
        return self.username
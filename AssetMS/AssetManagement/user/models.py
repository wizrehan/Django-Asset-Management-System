from django.db import models

class CreateUser(models.Model):
    username = models.CharField(max_length=100)
    
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    role_id = models.IntegerField()
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

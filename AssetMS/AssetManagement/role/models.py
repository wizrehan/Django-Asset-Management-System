from django.db import models

class RoleInsert(models.Model):
    role_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'role'

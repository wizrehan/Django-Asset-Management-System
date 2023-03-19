from django.db import models

# Create your models here.
class AddDepartment(models.Model):
    department_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)

    class Meta:
        db_table = 'department'
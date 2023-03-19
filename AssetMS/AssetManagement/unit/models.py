from django.db import models

# Create your models here.
class AddUnit(models.Model):
    unit_id = models.IntegerField() 
    unit_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=50)
    is_deleted = models.CharField(max_length=50)
    class Meta:
        db_table = 'unit' 

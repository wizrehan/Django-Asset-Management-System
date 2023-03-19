from django.db import models

# Create your models here.
class AddOfficeLocation(models.Model):
    address = models.CharField(max_length=200)
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
    class Meta:
        db_table = 'office_location'
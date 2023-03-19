from django.db import models

# Create your models here.
class AddManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
    class Meta:
        db_table = 'manufacturer'
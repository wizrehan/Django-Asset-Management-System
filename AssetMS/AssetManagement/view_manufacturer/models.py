from django.db import models

# Create your models here.

class ViewManufacture(models.Model):
    manufacturer_id = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    

        
    

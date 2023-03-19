from django.db import models

# Create your models here.

class ViewOffice(models.Model):
    office_location_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    

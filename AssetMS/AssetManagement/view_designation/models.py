from django.db import models

# Create your models here.

class ViewDes(models.Model):
    department_id = models.CharField(max_length=100)
    designation_name = models.CharField(max_length=100)
    
    

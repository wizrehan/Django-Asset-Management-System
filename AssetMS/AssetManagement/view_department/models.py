from django.db import models

# Create your models here.

class ViewDep(models.Model):
    department_id = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    
    

from django.db import models

# Create your models here.

class ViewCategory(models.Model):
    category_id = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    
    

        
    

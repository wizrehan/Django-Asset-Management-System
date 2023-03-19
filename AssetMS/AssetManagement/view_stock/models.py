from django.db import models

# Create your models here.

class ViewStoock(models.Model):
    stock_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    stock_in_date = models.CharField(max_length=100)
    available_stock = models.CharField(max_length=100)    
    

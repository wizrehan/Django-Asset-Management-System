from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings

# Create your models here.
class ReturnAsset(models.Model):
    product_id = models.IntegerField()
    employee_id = models.IntegerField()
    return_date = models.DateField()
    product_status = models.CharField(max_length=100)
    return_reason = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    received_by = models.CharField(max_length=100)
    countr = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'return_asset'
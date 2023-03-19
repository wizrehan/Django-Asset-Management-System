from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings

# Create your models here.
class ViewProductStatus(models.Model):
    status = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
    class Meta:
        db_table = 'product_status'
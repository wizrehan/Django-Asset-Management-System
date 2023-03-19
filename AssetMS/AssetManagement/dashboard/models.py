from django.db import models

# Create your models here.

class AssignDetails(models.Model):
    assign_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    comments = models.CharField(max_length=200)
    assign_date = models.CharField(max_length=100)

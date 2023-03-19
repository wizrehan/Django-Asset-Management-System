from django.db import models

# Create your models here.

class ViewEmp(models.Model):
    employee_id = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    designation_name = models.CharField(max_length=100)
    unit_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    emp_mail = models.CharField(max_length=100)
    office_loc = models.CharField(max_length=100)
    emp_status = models.CharField(max_length=100)
    

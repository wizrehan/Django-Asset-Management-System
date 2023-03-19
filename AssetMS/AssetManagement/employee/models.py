from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class ViewDep(models.Model):
    department_name = models.CharField(max_length=100)



class AddEmployee(models.Model):
    employee_id = models.BigIntegerField()
    employee_name = models.CharField(max_length=100)
    department_id = models.IntegerField()
    designation_id = models.IntegerField()
    unit_id = models.IntegerField()
    contact = models.CharField(max_length= 100)
    employee_mail = models.CharField(max_length= 100)
    office_location_id = models.IntegerField()
    employee_status = models.CharField(max_length=100)
    create_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)

    class Meta:
        db_table = 'employee'

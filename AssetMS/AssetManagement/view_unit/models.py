from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_id = models.IntegerField()
    unit_name = models.CharField(max_length=100)


    
    
# delete_choise=(
#     ('active','Active'),
#     ('deactive','Deactive'),

# )

# active_status=models.CharField(choices=delete_choise,default='active')
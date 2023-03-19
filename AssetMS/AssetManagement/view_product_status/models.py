from django.db import models

# Create your models here.

class ViewProdStatus(models.Model):
    product_status_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    


    
    

        
    

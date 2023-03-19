from django.db import models

# Create your models here.

class ViewProd(models.Model):
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    has_warrenty = models.CharField(max_length=100)
    warrenty_till = models.CharField(max_length=100)
    serial_IMEI = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    purchase_date = models.CharField(max_length=100) 
       
    

from django.db import models

# Create your models here.

class ViewVendor(models.Model):
    vendor_id = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_mail = models.CharField(max_length=100)
    vendor_location = models.CharField(max_length=100)
    Contact_person = models.CharField(max_length=100)
    vendor_type = models.CharField(max_length=100)
    vendor_status = models.CharField(max_length=100)
    has_trade = models.CharField(max_length=100)
    trade_document = models.ImageField()

        
    

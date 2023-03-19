from django.db import models

# Create your models here.
class AddVendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_mail = models.CharField(max_length=100)
    vendor_location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=300)
    vendor_type = models.CharField(max_length=100)
    vendor_status = models.CharField(max_length=100)
    has_trade = models.CharField(max_length=100)
    trade_document = models.FileField()
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
    class Meta:
        db_table = 'vendor'

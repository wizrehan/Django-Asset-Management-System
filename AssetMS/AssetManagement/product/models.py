from django.db import models
 
# Create your models here.
class AddProduct(models.Model):
    product_name = models.CharField(max_length=100)
    manufacture_id = models.IntegerField()
    category_id = models.IntegerField()
    vendor_id = models.IntegerField()
    warranty_till = models.DateField()
    serial_IMEI = models.CharField(max_length=100)
    specification  = models.CharField(max_length=500)
    invoice_no  = models.CharField(max_length=100)
    purchase_date = models.DateField()
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
   
    class Meta: 
        db_table = 'product' 

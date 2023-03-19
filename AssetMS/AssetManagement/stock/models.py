from django.db import models

# Create your models here.
class AddStock(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    stock_in_date = models.DateField()
    added_by = models.CharField(max_length=100)
    class Meta:
        db_table = 'stock'
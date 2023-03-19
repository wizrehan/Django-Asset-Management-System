from django.db import models

# Create your models here.
class ViewProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'product_category'
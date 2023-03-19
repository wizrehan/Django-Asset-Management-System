from django.db import models

class AssignAsset(models.Model):
    product_id = models.IntegerField()
    employee_id = models.IntegerField()
    assign_date = models.DateField()
    status  = models.CharField(max_length=100)
    comments = models.CharField(max_length=300)
    assigned_by = models.CharField(max_length=100)
    # quantity = models.IntegerField()
    # updatestockQuery = "update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.assign_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.quantity - B.idcount;"
    class Meta:
        db_table = 'assign_asset'
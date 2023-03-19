from django.db import models

class MakeRequistions(models.Model):
    product_id = models.IntegerField()
    employee_id = models.IntegerField()
    request_date = models.DateField(null=True, blank=True)
    message  = models.CharField(max_length=2000)
    request_by = models.CharField(max_length=100)
    is_accepted = models.CharField(max_length=100)
    accept_reject_by = models.CharField(max_length=100)
    feedback = models.CharField(max_length=2000)
    quantity = models.IntegerField()
    # updatestockQuery = "update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.assign_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.quantity - B.idcount;"
    class Meta:
        db_table = 'requisition'
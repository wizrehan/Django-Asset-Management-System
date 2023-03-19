from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from django.contrib.auth.decorators import login_required
from dashboard.models import AssignDetails
from assign_asset.models import AssignAsset
from assign_asset.filter import AssignedAssetFilter
from view_unit.models import Unit
from dashboard.decorators import allowed_user


# Create your views here. 
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def ViewReturnAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select ra.return_asset_id, p.product_name, e.employee_name, d.department_name, e.contact, p.warranty_till, ra.product_status, ra.return_reason, ra.comments,  ra.return_date, ra.received_by from assetmanager.return_asset ra  INNER JOIN assetmanager.product p on p.product_id=ra.product_id inner join assetmanager.employee e on e.employee_id=ra.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    asset = AssignAsset.objects.filter()
    filters = AssignedAssetFilter(request.GET, queryset = asset)

    updatestockQuery = "update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.return_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.available_stock + B.idcount;"
    c = cursor.execute(updatestockQuery)
    # results1 = cursor.fetchall()

    # print("--------Test Query",results1)
    
    return render(request, 'view/view_return_asset.html', {'ReturnDetails':results})
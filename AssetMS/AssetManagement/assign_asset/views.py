from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import mysql.connector as sql
from django.contrib import messages
from .models import AssignAsset
from .filter import AssignedAssetFilter

from datetime import date, time, datetime

 

product_id = ''
employee_id = ''
assign_date = ''
status = ''
comments = ''


# Create your views here.
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def assign_asset(request):
    
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    if request.method == "POST":
   
       if request.POST.get('product_id') and request.POST.get('employee_id') and request.POST.get('assign_date') and request.POST.get('status') and request.POST.get('comments'):
            
            
            saverecord = AssignAsset()
            saverecord.product_id = request.POST.get('product_id')
            saverecord.employee_id = request.POST.get('employee_id')
            saverecord.assign_date = request.POST.get('assign_date')
            saverecord.status = request.POST.get('status')
            saverecord.comments = request.POST.get('comments')
            saverecord.assigned_by = request.POST.get('assigned_by')
            # saverecord.quantity = request.POST.get('quantity')
            saverecord.save() 
            messages.success(request, "Asset Assigned Succesfully !")
            return render(request, 'pages/assign_asset.html')
              
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES' "
    cursor.execute(query)
    results = tuple(cursor.fetchall())

    query1 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES' "
    cursor.execute(query1)
    results1 = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.product_status"
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall()) 
    
    

    

    return render(request, "pages/assign_asset.html", {'ViewProduct':results, 'ViewEmp':results1, 'ViewProductStatus':results2})


#User Define funtion for search product 
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def SearchAsset(request):
    global employee_id, department_id, product_id, status, office_location_id, assign_date, fromdate, todate
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        department_id = request.POST.get('department_id')
        product_id = request.POST.get('product_id')
        status = request.POST.get('status')
        office_location_id = request.POST.get('office_location_id')
        assign_date = request.POST.get('assign_date')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print("..........Product Status = ", status)
        Asset = 'select p.product_name, e.employee_id, e.employee_name, d.department_name, ol.address, e.contact, ps.status, p.warranty_till, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id INNER JOIN assetmanager.product_status ps on ps.status = aa.status where p.product_id = '+product_id+' or aa.employee_id = '+employee_id+' or d.department_id = '+department_id+' or ol.office_location_id = '+office_location_id+' or aa.assign_date between "'+fromdate+'" and "'+todate+'" or aa.status = "'+status+'" '
        cursor.execute(Asset)
        AssetSearch = tuple(cursor.fetchall())

        
        query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
        cursor.execute(query1)
        getproduct = tuple(cursor.fetchall())

        query2 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES'"
        cursor.execute(query2)
        getemployee = tuple(cursor.fetchall())

        query3 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
        cursor.execute(query3)
        getdepartment = tuple(cursor.fetchall())

        query4 = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES'"
        cursor.execute(query4)
        getproductstatus = tuple(cursor.fetchall())

        query5 = "SELECT * FROM assetmanager.office_location ol where ol.is_deleted != 'YES'"
        cursor.execute(query5)
        getofficelocation = tuple(cursor.fetchall())



        
        return render(request, 'search/search_asset.html',{'SearchAsset':AssetSearch,'ViewProduct':getproduct, 'ViewEmployee':getemployee, 'ViewDepartment': getdepartment, 'ViewProStatus': getproductstatus, 'ViewOffice':getofficelocation})



    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    
    query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
    cursor.execute(query1)
    getproduct = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES'"
    cursor.execute(query2)
    getemployee = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(query3)
    getdepartment = tuple(cursor.fetchall())

    query4 = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES'"
    cursor.execute(query4)
    getproductstatus = tuple(cursor.fetchall())

    query5 = "SELECT * FROM assetmanager.office_location ol where ol.is_deleted != 'YES'"
    cursor.execute(query5)
    getofficelocation = tuple(cursor.fetchall())

    return render(request, 'search/search_asset.html',{ 'ViewProduct':getproduct, 'ViewEmployee':getemployee, 'ViewDepartment': getdepartment, 'ViewProStatus': getproductstatus, 'ViewOffice':getofficelocation})




@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def PrintSearchedAsset(request):
    
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print("..........Print Function() = ", 
        "product ID = ",product_id, 
        "Employee ID = ", employee_id,
        "Department ID = ", department_id, 
        "Status = ", status,
        "From Date = ", fromdate, 
        "To Date = ", todate,
        "Office Location = ", office_location_id)

        Asset = 'select p.product_name, e.employee_id, e.employee_name, d.department_name, ol.address, e.contact, ps.status, p.warranty_till, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id INNER JOIN assetmanager.product_status ps on ps.status = aa.status where p.product_id = '+product_id+' or aa.employee_id = '+employee_id+' or d.department_id = '+department_id+' or ol.office_location_id = '+office_location_id+' or aa.assign_date between "'+fromdate+'" and "'+todate+'" or aa.status = "'+status+'" '
        cursor.execute(Asset)
        AssetPrint = tuple(cursor.fetchall())
        # lst = {'employee_id':employee_id, 'department_id':department_id, 
        # 'product_id':product_id, 'status':status, 'office_location_id':office_location_id, 'assign_date':assign_date, 
        # 'fromdate':fromdate, 'todate':todate}

        today = date.today()
        dateformate = today.strftime("%B %d, %Y")
        # print("....... today = ", dateformate)

        currtime = datetime.now()
        timeformat = currtime.strftime("%I:%M %p")
        # print("....... Time = ", timeformat)

        return render(request, 'pdf/print_asset.html',{'PrintAsset':AssetPrint, "DATE":dateformate, "TIME":timeformat})











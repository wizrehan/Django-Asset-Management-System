from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from django.contrib.auth.decorators import login_required
from dashboard.models import AssignDetails
from assign_asset.models import AssignAsset
from assign_asset.filter import AssignedAssetFilter
from view_unit.models import Unit
from django.contrib import messages
# Create your views here. 


from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user

  
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def assigned_asset1(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()

    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    asset = AssignAsset.objects.filter()
    filters = AssignedAssetFilter(request.GET, queryset = asset)

    updatestockQuery = "update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.assign_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.quantity - B.idcount;"
    c = cursor.execute(updatestockQuery)
    results1 = cursor.fetchall()

    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall()) 

    print("--------Test Query",results1)
    
    return render(request, 'pages/assigned_asset.html', {'AssignDetails':results, 'filters':filters, 'QueryExecute':results1, 'GetStatus':results2 })
 

@ login_required(login_url='/')
def home1(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date from assetmanager.assign_asset aa INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id ;"
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    
    for i in request.user.groups.all():
                print("---------",i)
                Group = i
    set = 0
    # for j in Group:
    #     if j[0] == 'Department':
    #         get = 1
    print(".........Test = ", Group)
  
    return render(request, 'pages/home.html', {'AssignDetails':results, 'set':set, 'group':Group})


@ login_required(login_url='/')
@allowed_user(['admin'])
def create_user1(request):
    return render(request, 'pages/create_user.html')


@ login_required(login_url='/')
@allowed_user(['admin'])
def add_department1(request):
    return render(request, 'pages/add_department.html')

@ login_required(login_url='/')
@allowed_user(['admin'])
def add_designation1(request):
    return render(request, 'pages/add_designation.html')


@ login_required(login_url='/')
@allowed_user(['admin'])
def add_employee1(request):
    return render(request, 'pages/add_employee.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def add_manufacturer1(request):
    return render(request, 'pages/add_manufacturer.html')


@ login_required(login_url='/')
@allowed_user(['admin'])
def add_office_loc1(request):
    return render(request, 'pages/add_office_loc.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def add_product1(request):
    return render(request, 'pages/create_product.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def add_product_category1(request):
    return render(request, 'pages/add_product_category.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def add_product_status1(request):
    return render(request, 'pages/add_product_status.html') 

@ login_required(login_url='/')
@allowed_user(['admin'])
def create_role1(request):
    return render(request, 'pages/create_role.html')


@ login_required(login_url='/')
@allowed_user(['admin'])
def add_stock1(request):
    return render(request, 'pages/add_stock.html')


@ login_required(login_url='/')
@allowed_user(['admin'])
def add_unit1(request):
    return render(request, 'pages/add_unit.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def assign_asset1(request):
    return render(request, 'pages/assign_asset.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def add_vendor1(request):
    return render(request, 'pages/add_vendor.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_employee1(request):
    return render(request, 'view/view_employee.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_department1(request):
    return render(request, 'view/view_department.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_designation1(request):
    return render(request, 'view/view_designation.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_unit1(request):
    return render(request, 'view/view_unit.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_office_location1(request):
    return render(request, 'view/view_office_location.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_product1(request):
    return render(request, 'view/view_product.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_stock1(request):
    return render(request, 'view/view_stock.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_vendor1(request):
    return render(request, 'view/view_vendor.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_manufacturer1(request):
    return render(request, 'view/view_manufacturer.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_product_category1(request):
    return render(request, 'view/view_product_category.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def view_product_status1(request):
    return render(request, 'view/view_product_status.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def ViewCRUD1(request):
    return render(request, 'view/crud.html')

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def delete_items(request):
    return render(request, 'view/crud.html')


def Edit1(request, id):
    return render(request, 'pages/add_unit.html')


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def ReUsedAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Re-Used';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    # asset = AssignAsset.objects.filter()
    # filters = AssignedAssetFilter(request.GET, queryset = asset)
    
    return render(request, 'pages/reused_asset.html', {'ReUsedAsset':results, 'GetStatus':results2})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def UsedAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Used';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    # asset = AssignAsset.objects.filter()
    # filters = AssignedAssetFilter(request.GET, queryset = asset)

    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())
    
    return render(request, 'pages/used_asset.html', {'Usedasset':results, 'GetStatus':results2})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def DamagedAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select ra.return_asset_id, p.product_name, e.employee_name, d.department_name, e.contact, p.warranty_till, ra.product_status, ra.return_reason, ra.comments,  ra.return_date, ra.received_by from assetmanager.return_asset ra  INNER JOIN assetmanager.product p on p.product_id=ra.product_id inner join assetmanager.employee e on e.employee_id=ra.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where ra.product_status = 'Damaged';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    # asset = AssignAsset.objects.filter()
    # filters = AssignedAssetFilter(request.GET, queryset = asset)
    
    return render(request, 'pages/damaged_asset.html', {'DamagedAsset':results})

@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def RepairedAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Repaired';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    # asset = AssignAsset.objects.filter()
    # filters = AssignedAssetFilter(request.GET, queryset = asset)
    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())
    
    return render(request, 'pages/repaired_asset.html', {'RepairedAsset':results, 'GetStatus':results2})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def BrandNewAsset(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Brand New';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    # asset = AssignAsset.objects.filter()
    # filters = AssignedAssetFilter(request.GET, queryset = asset)
    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())
    
    return render(request, 'pages/brand_new_asset.html', {'BrandNewAsset':results, 'GetStatus':results2})


  


@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteAssignedAsset(request,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "Delete from assetmanager.assign_asset where assign_id =  %(assign_id)s"

    lst = {'assign_id':id}
    print("passing ID = ", id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Record Deleted !")
    
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id ; "
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    updatestockQuery = "update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.assign_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.quantity - B.idcount;"
    c = cursor.execute(updatestockQuery)
    results1 = cursor.fetchall()

    return render(request, 'pages/assigned_asset.html', {'AssignDetails':results, 'QueryExecute':results1 })





@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditAssignAsset(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST":
        getassignassetid = id
        getdate = request.POST.get('date')
        getstatus = request.POST.get('status')
        getcomments = request.POST.get('comments')
        

        print("-----Details - ", getdate, getstatus, getcomments)

        editassignedasset = 'update assetmanager.assign_asset aa set aa.assign_date = "'+getdate+'" , aa.status = "'+getstatus+'" , aa.comments = "'+getcomments+'" ,  aa.delete_edited_by = %(delete_edited_by)s where aa.assign_id = "'+getassignassetid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editassignedasset,lst) 
        m.commit()

        messages.success(request, "Assigned Asset Updated !")

        c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
        cursor.execute(query2)
        results2 = tuple(cursor.fetchall())

        return render(request, 'pages/assigned_asset.html', {'AssignDetails':results, 'GetStatus':results2 })






@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteUsedAsset(request,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "Delete from assetmanager.assign_asset where assign_id =  %(assign_id)s"

    lst = {'assign_id':id}
    print("passing ID = ", id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Record Deleted !")
    
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Used' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    return render(request, 'pages/used_asset.html', {'Usedasset':results, 'GetStatus':results2 })



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditUsedAsset(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST":
        getassignassetid = id 
        getdate = request.POST.get('date')
        getstatus = request.POST.get('status')
        getcomments = request.POST.get('comments')
         

        print("-----Details - ", getdate, getstatus, getcomments)

        editassignedasset = 'update assetmanager.assign_asset aa set aa.assign_date = "'+getdate+'" , aa.status = "'+getstatus+'" , aa.comments = "'+getcomments+'" ,  aa.delete_edited_by = %(delete_edited_by)s where aa.assign_id = "'+getassignassetid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editassignedasset,lst) 
        m.commit()

        messages.success(request, "Used Asset Updated !")

        c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Used' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
        cursor.execute(query2)
        results2 = tuple(cursor.fetchall())

        return render(request, 'pages/used_asset.html', {'Usedasset':results, 'GetStatus':results2 })




@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteReUsedAsset(request,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "Delete from assetmanager.assign_asset where assign_id =  %(assign_id)s"

    lst = {'assign_id':id}
    print("passing ID = ", id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Record Deleted !")
    
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Re-Used' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    return render(request, 'pages/reused_asset.html', {'ReUsedAsset':results, 'GetStatus':results2})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditReUsedAsset(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST": 
        getassignassetid = id 
        getdate = request.POST.get('date')
        getstatus = request.POST.get('status')
        getcomments = request.POST.get('comments')
         

        print("-----Details - ", getdate, getstatus, getcomments)

        editassignedasset = 'update assetmanager.assign_asset aa set aa.assign_date = "'+getdate+'" , aa.status = "'+getstatus+'" , aa.comments = "'+getcomments+'" ,  aa.delete_edited_by = %(delete_edited_by)s where aa.assign_id = "'+getassignassetid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editassignedasset,lst) 
        m.commit() 

        messages.success(request, "Re-Used Asset Updated !")

        c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Re-Used' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
        cursor.execute(query2)
        results2 = tuple(cursor.fetchall())

        return render(request, 'pages/reused_asset.html', {'ReUsedAsset':results, 'GetStatus':results2})





@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteRepairedAsset(request,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "Delete from assetmanager.assign_asset where assign_id =  %(assign_id)s"

    lst = {'assign_id':id}
    print("passing ID = ", id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Record Deleted !")
    
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Repaired' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    return render(request, 'pages/repaired_asset.html', {'RepairedAsset':results, 'GetStatus':results2})




@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditRepairedAsset(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST":
        getassignassetid = id  
        getdate = request.POST.get('date')
        getstatus = request.POST.get('status')
        getcomments = request.POST.get('comments')
         

        print("-----Details - ", getdate, getstatus, getcomments)

        editassignedasset = 'update assetmanager.assign_asset aa set aa.assign_date = "'+getdate+'" , aa.status = "'+getstatus+'" , aa.comments = "'+getcomments+'" ,  aa.delete_edited_by = %(delete_edited_by)s where aa.assign_id = "'+getassignassetid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editassignedasset,lst) 
        m.commit() 

        messages.success(request, "Repaired Asset Updated !")

        c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Repaired' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
        cursor.execute(query2)
        results2 = tuple(cursor.fetchall())

        return render(request, 'pages/repaired_asset.html', {'RepairedAsset':results, 'GetStatus':results2})



@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteBrandNewAsset(request,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "Delete from assetmanager.assign_asset where assign_id =  %(assign_id)s"

    lst = {'assign_id':id}
    print("passing ID = ", id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Record Deleted !")
    
    cursor = m.cursor()
    c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Brand New'; "
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    return render(request, 'pages/brand_new_asset.html', {'BrandNewAsset':results})




@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditBrandNewAsset(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST":
        getassignassetid = id 
        getdate = request.POST.get('date')
        getstatus = request.POST.get('status')
        getcomments = request.POST.get('comments')
         

        print("-----Details - ", getdate, getstatus, getcomments)

        editassignedasset = 'update assetmanager.assign_asset aa set aa.assign_date = "'+getdate+'" , aa.status = "'+getstatus+'" , aa.comments = "'+getcomments+'" ,  aa.delete_edited_by = %(delete_edited_by)s where aa.assign_id = "'+getassignassetid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editassignedasset,lst) 
        m.commit() 

        messages.success(request, "Brand New Asset Updated !")

        c = "select aa.assign_id, p.product_name, p.warranty_till, e.employee_name, d.department_name, ol.address, e.contact, aa.status, aa.comments, aa.assign_date, aa.assigned_by from assetmanager.assign_asset aa  INNER JOIN assetmanager.product p on p.product_id=aa.product_id inner join assetmanager.employee e on e.employee_id=aa.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.office_location ol on ol.office_location_id = e.office_location_id where aa.status = 'Brand New' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query2 = "SELECT * FROM assetmanager.product_status  p where p.is_deleted != 'YES' "
        cursor.execute(query2)
        results2 = tuple(cursor.fetchall())

        return render(request, 'pages/brand_new_asset.html', {'BrandNewAsset':results, 'GetStatus':results2})




def test(request):
    return render(request, 'pages/index.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from django.contrib import messages 
from product.models import AddProduct
from datetime import date, time, datetime
from .models import MakeRequistions
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
import json
@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
# Create your views here.

 

def MakeRequisition(request, user):
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    print(".....BEfore IF Condition")
    if request.method == "POST":
       print(".....After IF Condition")
       if  request.POST.get('employee_id') and request.POST.get('product_id'):
            currtime = datetime.now()
            # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
            timeformat = currtime.strftime("%Y-%m-%d")
            
            saverecord = MakeRequistions() 
            print("....TEST", request.POST.get('product_id'), request.POST.get('employee_id'), request.POST.get('request_date') )
            saverecord.product_id = request.POST.get('product_id')
            saverecord.employee_id = request.POST.get('employee_id')
            saverecord.request_date = timeformat
            saverecord.message = request.POST.get('message') 
            saverecord.request_by = user
            saverecord.is_accepted = 'NO'
            saverecord.quantity = request.POST.get('quantity')
            saverecord.save()

            messages.success(request, "Requistion Done !")


            c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id where p.is_deleted != "YES" order by p.product_id desc '
            cursor.execute(c)
            viewproduct = tuple(cursor.fetchall())

            
            query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
            cursor.execute(query1)
            getproduct = tuple(cursor.fetchall())

            query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
            cursor.execute(query2)
            getvendor = tuple(cursor.fetchall())

            query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
            cursor.execute(query3)
            getmanufacturer = tuple(cursor.fetchall())

            query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
            cursor.execute(query4)
            getproductcategory = tuple(cursor.fetchall())

            query5 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES'"
            cursor.execute(query5)
            getemployee = tuple(cursor.fetchall())

            currtime = datetime.now()
            # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
            timeformat = currtime.strftime("%Y-%m-%d")
            print(".....Date", timeformat)


            return render(request, 'view/view_list_product.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 

              

    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()

    c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id where p.is_deleted != "YES" order by p.product_id desc'
    cursor.execute(c)
    viewproduct = tuple(cursor.fetchall())

    
    query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
    cursor.execute(query1)
    getproduct = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(query2)
    getvendor = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
    cursor.execute(query3)
    getmanufacturer = tuple(cursor.fetchall())

    query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(query4)
    getproductcategory = tuple(cursor.fetchall())

    query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = '+user+' '
    cursor.execute(query5)
    getemployee = tuple(cursor.fetchall())

    currtime = datetime.now()
    # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
    timeformat = currtime.strftime("%Y-%m-%d")
    print(".....Date", timeformat)

    messages.error(request, "Something IS Worng !!")
    return render(request, 'view/view_list_product.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 






def ViewListProduct(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "select p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, 'YES', 'NO') as has_warranty from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id where p.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_list_product.html', {'ViewProd':results})





#User Define funtion for search product 
@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
def GETProduct(request, user):
    global product_name, category_id, haswarranty, nowarranty
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        category_id = request.POST.get('category_id')
        haswarranty = 'YES'
        nowarranty = 'NO'
         
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print(".... TEST",product_name, category_id )

        PRODUCT = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id  where  (((p.product_name  like  "%'+product_name+'%") or (p.specification like "%'+product_name+'%")) or p.category_id = "'+category_id+'") and p.is_deleted != "YES" order by p.product_id desc ' 
        cursor.execute(PRODUCT)
        ProductSearch = tuple(cursor.fetchall())

        
        query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
        cursor.execute(query1)
        getproduct = tuple(cursor.fetchall())

        query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
        cursor.execute(query2)
        getvendor = tuple(cursor.fetchall())

        query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
        cursor.execute(query3)
        getmanufacturer = tuple(cursor.fetchall())

        query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
        cursor.execute(query4)
        getproductcategory = tuple(cursor.fetchall())

        query5 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES'"
        cursor.execute(query5)
        getemployee = tuple(cursor.fetchall())

        currtime = datetime.now()
        timeformat = currtime.strftime("%Y-%m-%d")

        

        
        return render(request, 'view/view_list_product.html',{'DateTime':timeformat,'GetEMP':getemployee, 'GetProduct':ProductSearch,'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory})
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
 
    c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id  where p.is_deleted != "YES" order by p.product_id desc '
    cursor.execute(c)
    viewproduct = tuple(cursor.fetchall())

    
    query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
    cursor.execute(query1)
    getproduct = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(query2)
    getvendor = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
    cursor.execute(query3)
    getmanufacturer = tuple(cursor.fetchall())

    query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(query4)
    getproductcategory = tuple(cursor.fetchall())

    query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'" '
    cursor.execute(query5)
    getemployee = tuple(cursor.fetchall())

    currtime = datetime.now()
    # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
    timeformat = currtime.strftime("%Y-%m-%d")
    print(".....Date", timeformat)

    return render(request, 'view/view_list_product.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 





#User Define funtion for search product 
@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
def ViewRequestedAsset(request):
    global product_name, category_id, haswarranty, nowarranty
    if request.method == "POST":
        department_id = request.POST.get('department_id')
        category_id = request.POST.get('category_id')
        unit_id = request.POST.get('unit_id') 
        
        
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print(".... TEST",department_id, category_id, unit_id )

        GetSearch = 'select r.requisition_id, p.product_id, p.product_name, e.employee_name, d.department_name , p.specification, s.available_stock, r.quantity, r.request_by, r.request_date, r.message , r.feedback , r.is_accepted from assetmanager.requisition r INNER JOIN assetmanager.employee e on e.employee_id = r.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.product p on p.product_id = r.product_id Inner join assetmanager.stock s on s.product_id = p.product_id where  e.department_id = "'+department_id+'" or e.unit_id = "'+unit_id+'" or p.category_id = "'+category_id+'" order by r.requisition_id desc ' 
        cursor.execute(GetSearch)
        RequestedProductSearch = tuple(cursor.fetchall())


        query1 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
        cursor.execute(query1)
        getproductcategory = tuple(cursor.fetchall())

        query2 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
        cursor.execute(query2)
        getdepartment = tuple(cursor.fetchall())

        query3 = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES'"
        cursor.execute(query3)
        getunit = tuple(cursor.fetchall())
        

        
        return render(request, 'view/view_requested_asset.html',{'GetRequestedProduct':RequestedProductSearch, 'ViewCategory': getproductcategory, 'ViewDepartment': getdepartment, 'ViewUnit': getunit})
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()

    c = 'select r.requisition_id, p.product_id, p.product_name, e.employee_name, d.department_name , p.specification, s.available_stock, r.quantity, r.request_by, r.request_date, r.message , r.feedback , r.is_accepted from assetmanager.requisition r INNER JOIN assetmanager.employee e on e.employee_id = r.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.product p on p.product_id = r.product_id Inner join assetmanager.stock s on s.product_id = p.product_id order by r.requisition_id desc '
    cursor.execute(c)
    RequestedProductSearch = tuple(cursor.fetchall())

    
    query1 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(query1)
    getproductcategory = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(query2)
    getdepartment = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES'"
    cursor.execute(query3)
    getunit = tuple(cursor.fetchall())

    

    return render(request, 'view/view_requested_asset.html',{'GetRequestedProduct':RequestedProductSearch, 'ViewCategory': getproductcategory, 'ViewDepartment': getdepartment, 'ViewUnit': getunit})







@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def AcceptRequisition(request,id,user):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    print(".....BEfore IF Condition")
    if request.method == "POST":
       print(".....After IF Condition")
       if  request.POST.get('feedback'):
            

            getfeedback = request.POST.get('feedback')
            requid = id
            print("......requisition ID = ", requid, "\n ... Type = ", type(requid))
            print("....TEST", getfeedback, int(id), user)

            acceptrequest = 'update assetmanager.requisition r set  r.is_accepted ="Accepted" , r.feedback = "'+getfeedback+'",  r.accept_reject_by = %(accept_reject_by)s where r.requisition_id = "'+requid+'"  '
            
            lst = {'accept_reject_by':user}
            cursor.execute(acceptrequest,lst) 
            m.commit()

            messages.success(request, "Requistion Accepted !")

                
            c = 'select r.requisition_id, p.product_id, p.product_name, e.employee_name, d.department_name , p.specification, s.available_stock, r.quantity, r.request_by, r.message , r.feedback , r.is_accepted from assetmanager.requisition r INNER JOIN assetmanager.employee e on e.employee_id = r.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.product p on p.product_id = r.product_id Inner join assetmanager.stock s on s.product_id = p.product_id order by r.requisition_id desc '
            cursor.execute(c)
            RequestedProductSearch = tuple(cursor.fetchall())

                
            query1 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
            cursor.execute(query1)
            getproductcategory = tuple(cursor.fetchall())

            query2 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
            cursor.execute(query2)
            getdepartment = tuple(cursor.fetchall())

            query3 = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES'"
            cursor.execute(query3)
            getunit = tuple(cursor.fetchall())

            return render(request, 'view/view_requested_asset.html',{'GetRequestedProduct':RequestedProductSearch, 'ViewCategory': getproductcategory, 'ViewDepartment': getdepartment, 'ViewUnit': getunit})





@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def RejectRequisition(request,id,user):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    print(".....BEfore IF Condition")
    if request.method == "POST":
       print(".....After IF Condition")
       if  request.POST.get('feedback'):
            

            getfeedback = request.POST.get('feedback')
            requid = id
            print("......requisition ID = ", requid, "\n ... Type = ", type(requid))
            print("....TEST", getfeedback, int(id), user)

            acceptrequest = 'update assetmanager.requisition r set  r.is_accepted ="Rejected" , r.feedback = "'+getfeedback+'",  r.accept_reject_by = %(accept_reject_by)s where r.requisition_id = "'+requid+'" '
            
            lst = {'accept_reject_by':user}
            cursor.execute(acceptrequest,lst) 
            m.commit()

            messages.error(request, "Requistion Rejected !")

                
            c = 'select r.requisition_id, p.product_id, p.product_name, e.employee_name, d.department_name , p.specification, s.available_stock, r.quantity, r.request_by, r.message , r.feedback , r.is_accepted from assetmanager.requisition r INNER JOIN assetmanager.employee e on e.employee_id = r.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.product p on p.product_id = r.product_id Inner join assetmanager.stock s on s.product_id = p.product_id order by r.requisition_id desc '
            cursor.execute(c)
            RequestedProductSearch = tuple(cursor.fetchall())

                
            query1 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
            cursor.execute(query1)
            getproductcategory = tuple(cursor.fetchall())

            query2 = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
            cursor.execute(query2)
            getdepartment = tuple(cursor.fetchall())

            query3 = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES'"
            cursor.execute(query3)
            getunit = tuple(cursor.fetchall())

            return render(request, 'view/view_requested_asset.html',{'GetRequestedProduct':RequestedProductSearch, 'ViewCategory': getproductcategory, 'ViewDepartment': getdepartment, 'ViewUnit': getunit})



 


@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
def ViewDepartmentRequest(request,user):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()

    getuser = user 

    c = 'select r.requisition_id, p.product_id, p.product_name, e.employee_name, d.department_name , p.specification, s.available_stock, r.quantity, r.request_by, r.request_date, r.message , r.feedback , r.is_accepted from assetmanager.requisition r INNER JOIN assetmanager.employee e on e.employee_id = r.employee_id INNER JOIN assetmanager.department d on d.department_id = e.department_id INNER JOIN assetmanager.product p on p.product_id = r.product_id Inner join assetmanager.stock s on s.product_id = p.product_id  where r.request_by = "'+getuser+'" order by r.requisition_id desc '
    cursor.execute(c)
    RequestedProductSearch = tuple(cursor.fetchall())

                
    

    return render(request, 'view/view_user_requested_asset.html',{'GetUserRequestedProduct':RequestedProductSearch})








@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
def MakeRequisitionTEST(request, user):
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    selected = []
    get = []

    print(".....BEfore IF Condition")
    if request.method == "POST": 
        print(".....After IF Condition")
        
        # get product id as int list
        selected = request.POST.getlist('selected[]')
        print("...Type",type(selected))
        newlist = []
        for word in selected:
            word = word.split(",")
            newlist.extend(word)

        
        #to convert garveg list to number 
        getq = []
        getq = request.POST.getlist('values[]')
        print("......Quantity =", getq )
        getquantity = list(filter(lambda x: x != '', getq))
        cleaned_list = []
        for i in getquantity:
            i = i.split(",")
            for j in i:
                if j.isdigit():
                    cleaned_list.append(int(j))
        print("---cleaned list", cleaned_list)


      
        print("......selected =", selected )
        print("......Splited =", newlist )
        getmsz = request.POST.get('message')
        print("......Message =", getmsz )
        

        currtime = datetime.now()
        # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
        timeformat = currtime.strftime("%Y-%m-%d")

        empid = 'SELECT e.employee_id FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'"'
        cursor.execute(empid)
        getempid = list(cursor.fetchone())
        
        print(".....Employee_ID = ", getempid[0])
        for (i,j) in zip(newlist,cleaned_list):
            saverecord = MakeRequistions() 
            print("....TEST Requisition", i, j, user )
            saverecord.product_id = i
            saverecord.employee_id = getempid[0]
            saverecord.request_date = timeformat
            saverecord.message = request.POST.get('message') 
            saverecord.request_by = user
            saverecord.is_accepted = 'NO' 
            saverecord.quantity = j
            saverecord.save()

        messages.success(request, "Requistion Done !")


        c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id where p.is_deleted != "YES" '
        cursor.execute(c)
        viewproduct = tuple(cursor.fetchall())

        
        query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
        cursor.execute(query1)
        getproduct = tuple(cursor.fetchall())

        query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
        cursor.execute(query2)
        getvendor = tuple(cursor.fetchall())

        query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
        cursor.execute(query3)
        getmanufacturer = tuple(cursor.fetchall())

        query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
        cursor.execute(query4)
        getproductcategory = tuple(cursor.fetchall())

        query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'"'
        cursor.execute(query5)
        getemployee = tuple(cursor.fetchall())

        currtime = datetime.now()
        # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
        timeformat = currtime.strftime("%Y-%m-%d")
        print(".....Date", timeformat)


        return render(request, 'view/view_list_product_test.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 

              

    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()

    c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id where p.is_deleted != "YES" '
    cursor.execute(c)
    viewproduct = tuple(cursor.fetchall())

    
    query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
    cursor.execute(query1)
    getproduct = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(query2)
    getvendor = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
    cursor.execute(query3)
    getmanufacturer = tuple(cursor.fetchall())

    query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(query4)
    getproductcategory = tuple(cursor.fetchall())

    query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'" '
    cursor.execute(query5)
    getemployee = tuple(cursor.fetchall())

    currtime = datetime.now()
    # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
    timeformat = currtime.strftime("%Y-%m-%d")
    print(".....Date", timeformat)

    messages.error(request, "Something IS Worng !!")
    return render(request, 'view/view_list_product_test.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 






#User Define funtion for search product 
@ login_required(login_url='/')
@allowed_user(['admin', 'user', 'Department'])
def GETProductTEST(request, user):
    global product_name, category_id, haswarranty, nowarranty
    if request.method == "POST":
        
        product_name = request.POST.get('product_name')
        category_id = request.POST.get('category_id')
        haswarranty = 'YES'
        nowarranty = 'NO'
         
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print(".... TEST",product_name, category_id )

        PRODUCT = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id  where  (((p.product_name  like  "%'+product_name+'%") or (p.specification like "%'+product_name+'%")) or p.category_id = "'+category_id+'") and p.is_deleted != "YES" order by p.product_id desc  ' 
        cursor.execute(PRODUCT)
        ProductSearch = tuple(cursor.fetchall())

        
        query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
        cursor.execute(query1)
        getproduct = tuple(cursor.fetchall())

        query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
        cursor.execute(query2)
        getvendor = tuple(cursor.fetchall())

        query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
        cursor.execute(query3)
        getmanufacturer = tuple(cursor.fetchall())

        query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
        cursor.execute(query4)
        getproductcategory = tuple(cursor.fetchall())

        query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'"'
        cursor.execute(query5)
        getemployee = tuple(cursor.fetchall())

        currtime = datetime.now()
        timeformat = currtime.strftime("%Y-%m-%d")

        

        
        return render(request, 'view/view_list_product_test.html',{'DateTime':timeformat,'GetEMP':getemployee, 'GetProduct':ProductSearch,'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory})
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
  
    c = 'select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, p.specification, if(now()<p.warranty_till, "YES", "NO") as has_warranty, if(s.available_stock != 0, "YES", "NO") as Has_Stock from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id Inner join assetmanager.stock s on s.product_id = p.product_id where p.is_deleted != "YES" '
    cursor.execute(c)
    viewproduct = tuple(cursor.fetchall())

    
    query1 = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES'"
    cursor.execute(query1)
    getproduct = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(query2)
    getvendor = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.manufacturer m where m.is_deleted != 'YES'"
    cursor.execute(query3)
    getmanufacturer = tuple(cursor.fetchall())

    query4 = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(query4)
    getproductcategory = tuple(cursor.fetchall())

    query5 = 'SELECT * FROM assetmanager.employee e inner join assetmanager.auth_user au on au.employee_id = e.employee_id  where e.is_deleted != "YES" and au.username = "'+user+'" '
    cursor.execute(query5)
    getemployee = tuple(cursor.fetchall())

    currtime = datetime.now()
    # timeformat = currtime.strftime(" %d/%m/%Y |  %r")
    timeformat = currtime.strftime("%Y-%m-%d")
    print(".....Date", timeformat)

    return render(request, 'view/view_list_product_test.html',{'DateTime':timeformat, 'GetProduct':viewproduct, 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory, 'GetEMP':getemployee}) 




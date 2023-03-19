from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewProd
from product.models import AddProduct
from datetime import date, time, datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.


def ViewProduct(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, v.vendor_name, p.warranty_till, p.serial_IMEI, p.specification, p.invoice_no, p.purchase_date, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id where p.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    getcat = "select * from assetmanager.product_category pc where pc.is_deleted != 'YES'"
    cursor.execute(getcat)
    viewcat = tuple(cursor.fetchall())

    getmanu = "select * from assetmanager.manufacturer m where m.is_deleted != 'YES'"
    cursor.execute(getmanu)
    viewmanu = tuple(cursor.fetchall())

    getvendor = "select * from assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(getvendor)
    viewvendor = tuple(cursor.fetchall())

    return render(request, 'view/view_product.html', {'ViewProd':results, 'ViewCAT':viewcat, 'ViewMANU':viewmanu, 'ViewVendor':viewvendor})

 

# def DeleteProduct(request,id):

#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     d = 'Delete from assetmanager.product where product_id =  %(product_id)s'
#     # tup = list[id]
#     lst = {'product_id':id}
#     print("passing ID = ", id)
#     cursor.execute(d,lst)
#     m.commit()

    
#     c = "select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, v.vendor_name, p.warranty_till, p.serial_IMEI, p.specification, p.invoice_no, p.purchase_date, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id ; "
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())
#     return render(request, 'view/view_product.html', {'ViewProd':results})

@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteProduct(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.product p set p.is_deleted = 'YES', p.delete_edited_by = %(delete_edited_by)s  where product_id = %(product_id)s"

    lst = {'delete_edited_by':user,'product_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()

    messages.error(request, "Product Deleted !")
    cursor = m.cursor()
    c = "select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, v.vendor_name, p.warranty_till, p.serial_IMEI, p.specification, p.invoice_no, p.purchase_date, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id where p.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_product.html', {'ViewProd':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditProduct(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getproductid = id
        getuser = user
        getproduct = request.POST.get('product_name')
        getcat = request.POST.get('category_id')
        getmanu = request.POST.get('manufacturer_id')
        getvendor = request.POST.get('vendor_id')
        getspec = request.POST.get('specification')
        getserial = request.POST.get('serial_IMEI')
        getinvoice = request.POST.get('invoice_no')
        getpurchase = request.POST.get('purchase_date')
        getwarranty = request.POST.get('warranty_till')

        

        print("-----Details - ", getproductid, getuser, getproduct, getcat, getmanu, getvendor, getspec, getserial, getinvoice, getpurchase, getwarranty) 
 
        editproduct = 'update assetmanager.product p set p.product_name = "'+getproduct+'" , p.category_id = "'+getcat+'", p.manufacture_id = "'+getmanu+'" , p.vendor_id = "'+getvendor+'" , p.specification = "'+getspec+'" , p.serial_IMEI = "'+getserial+'", p.invoice_no = "'+getinvoice+'" , p.warranty_till = "'+getwarranty+'", p.purchase_date = "'+getpurchase+'" , p.delete_edited_by = "'+getuser+'" where p.product_id = "'+getproductid+'"'
        cursor.execute(editproduct) 
        m.commit()
        messages.success(request, "Product Updated!")

        c = "select p.product_id, p.product_name, pc.category_name,  m.manufacturer_name, v.vendor_name, p.warranty_till, p.serial_IMEI, p.specification, p.invoice_no, p.purchase_date, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id where p.is_deleted != 'YES'"
        cursor.execute(c)
        results = tuple(cursor.fetchall())

        getcat = "select * from assetmanager.product_category pc where pc.is_deleted != 'YES'"
        cursor.execute(getcat)
        viewcat = tuple(cursor.fetchall())

        getmanu = "select * from assetmanager.manufacturer m where m.is_deleted != 'YES'"
        cursor.execute(getmanu)
        viewmanu = tuple(cursor.fetchall())

        getvendor = "select * from assetmanager.vendor v where v.is_deleted != 'YES'"
        cursor.execute(getvendor)
        viewvendor = tuple(cursor.fetchall())

        return render(request, 'view/view_product.html', {'ViewProd':results, 'ViewCAT':viewcat, 'ViewMANU':viewmanu, 'ViewVendor':viewvendor})




#User Define funtion for search product 
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def SearchProduct(request):
    global product_id, vendor_id, manufacturer_id, category_id, invoice_no
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        vendor_id = request.POST.get('vendor_id')
        manufacturer_id = request.POST.get('manufacturer_id')
        category_id = request.POST.get('category_id')
        invoice_no = request.POST.get('invoice_no')
        
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()

        PRODUCT = 'select p.product_name, v.vendor_name, m.manufacturer_name, pc.category_name, s.available_stock, s.quantity, p.purchase_date,  p.warranty_till, p.specification, p.serial_IMEI,  p.invoice_no, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id INNER JOIN assetmanager.stock s on s.product_id = p.product_id where  v.vendor_id = '+vendor_id+' or p.product_id = '+product_id+' or  m.manufacturer_id = '+manufacturer_id+' or p.category_id = '+category_id+' or p.invoice_no = '+invoice_no+' '
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



        
        return render(request, 'search/search_product.html',{'SearchProduct':ProductSearch,'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory})
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    
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

    return render(request, 'search/search_product.html',{ 'ViewProduct':getproduct, 'ViewVendor':getvendor, 'ViewManufacture': getmanufacturer, 'ViewCategory': getproductcategory}) 





@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def PrintSearchedProduct(request):
    
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print("..........Print Function() = ", 
        "product ID = ",product_id, 
        "Vendor ID = ", vendor_id,
        "Manufacturer ID = ", manufacturer_id, 
        "Category ID = ", category_id,
        "Invoice No.  = ", invoice_no)

        PRODUCT = 'select p.product_name, v.vendor_name, m.manufacturer_name, s.available_stock, s.quantity, p.purchase_date,  p.warranty_till, p.specification, p.serial_IMEI,  p.invoice_no, p.added_by  from assetmanager.product p INNER JOIN assetmanager.manufacturer m on m.manufacturer_id = p.manufacture_id INNER JOIN assetmanager.product_category pc on pc.category_id=p.category_id  INNER JOIN assetmanager.vendor v on v.vendor_id = p.vendor_id INNER JOIN assetmanager.stock s on s.product_id = p.product_id where  v.vendor_id = '+vendor_id+' or p.product_id = '+product_id+' or  m.manufacturer_id = '+manufacturer_id+' or p.category_id = '+category_id+' or p.invoice_no = '+invoice_no+' '
        cursor.execute(PRODUCT)
        ProductSearch = tuple(cursor.fetchall())
        # lst = {'employee_id':employee_id, 'department_id':department_id, 
        # 'product_id':product_id, 'status':status, 'office_location_id':office_location_id, 'assign_date':assign_date, 
        # 'fromdate':fromdate, 'todate':todate}

        today = date.today()
        dateformate = today.strftime("%B %d, %Y")
        # print("....... today = ", dateformate)

        currtime = datetime.now()
        timeformat = currtime.strftime("%I:%M %p")
        # print("....... Time = ", timeformat)

        return render(request, 'pdf/print_product.html',{'PrintProduct':ProductSearch, "DATE":dateformate, "TIME":timeformat})
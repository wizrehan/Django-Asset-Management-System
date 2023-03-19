from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from django.contrib.auth.models import User 
from datetime import date, time, datetime
from django.contrib import messages 

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.


def ViewStock(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "select s.stock_id, p.product_name, s.quantity, s.stock_in_date, s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id order by s.stock_id desc ; "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    


    cursor = m.cursor()
    first = "update  assetmanager.return_asset as ra , assetmanager.stock s  inner join (select product_id, count(product_id) as idcount from assetmanager.return_asset group by product_id ) as B on B.product_id = s.product_id set s.available_stock = if (ra.countr = 'NO', s.available_stock + B.idcount , ra.countr = 'YES')  ;"
    second= 'update assetmanager.stock s inner join (select product_id, count(product_id) idcount from assetmanager.assign_asset group by product_id) as B on B.product_id = s.product_id set s.available_stock = s.quantity - B.idcount;'
    third = "update  assetmanager.return_asset as ra , assetmanager.stock s  inner join (select product_id, count(product_id) as idcount from assetmanager.return_asset group by product_id ) as B on B.product_id = s.product_id set s.available_stock = if (ra.countr = 'NO', s.available_stock + B.idcount , ra.countr = 'YES')  ;"
    cursor.execute(first)
    cursor.execute(second)
    cursor.execute(third)
    m.commit()

    return render(request, 'view/view_stock.html', {'ViewStoock':results})





@ login_required(login_url='/')
@allowed_user(['admin'])

def DeleteStock(request,id):

    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = 'Delete from assetmanager.stock where stock_id =  %(stock_id)s'
    # tup = list[id]
    lst = {'stock_id':id}
    print("passing ID = ", id)
    cursor.execute(c,lst)
    m.commit()
    messages.error(request, "Stock Deleted !")

    
    c = "select s.stock_id, p.product_name, s.quantity, s.stock_in_date, s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id order by s.stock_id desc ;"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_stock.html', {'ViewStoock':results})



 
@ login_required(login_url='/')
@allowed_user(['admin'])
def EditStock(request, id):

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST":
        getstockid = id
        getstockindate = request.POST.get('stock_in_date')
        quantity = request.POST.get('quantity')

        print("-----Details - ", getstockid, getstockindate, quantity)

        editstock = 'update assetmanager.stock s set s.stock_in_date = "'+getstockindate+'" ,  s.quantity ="'+quantity+'"  where s.stock_id = "'+getstockid+'"'
        cursor.execute(editstock) 
        m.commit()
        messages.success(request, "Stock Edited !")

        c = "select s.stock_id, p.product_name, s.quantity, s.stock_in_date, s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id order by s.stock_id desc ;"
        cursor.execute(c)
        results = tuple(cursor.fetchall())


        return render(request, 'view/view_stock.html', {'ViewStoock':results})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def SearchStock(request):
    global vendor_id
    if request.method == "POST":
        vendor_id = request.POST.get('vendor_id')
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print("....SerachVendor Id - ", vendor_id)
        if vendor_id != 'null':
            stock = 'select s.stock_id, p.product_name, v.vendor_name, s.quantity, s.stock_in_date, (s.quantity - s.available_stock) as total_assigned,  s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id inner join assetmanager.vendor v on v.vendor_id = p.vendor_id where v.vendor_id = '+vendor_id+' order by s.stock_id desc; '
            cursor.execute(stock)
            viewstock = tuple(cursor.fetchall())

        else:
            stock = 'select s.stock_id, p.product_name, v.vendor_name, s.quantity, s.stock_in_date, (s.quantity - s.available_stock) as total_assigned,  s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id inner join assetmanager.vendor v on v.vendor_id = p.vendor_id where v.vendor_id != "null"  order by s.stock_id desc; '
            cursor.execute(stock)
            viewstock = tuple(cursor.fetchall())

        
        query = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
        cursor.execute(query)
        results = tuple(cursor.fetchall()) 

        
        return render(request, 'search/search_stock.html',{'ViewVendor':results, 'ViewStock':viewstock })
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor() 
    query = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(query)
    results = tuple(cursor.fetchall())

    s = "select s.stock_id, p.product_name, v.vendor_name, s.quantity, s.stock_in_date, (s.quantity - s.available_stock) as total_assigned,  s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id inner join assetmanager.vendor v on v.vendor_id = p.vendor_id order by s.stock_id desc "
    cursor.execute(s)
    viewstock = tuple(cursor.fetchall())


    return render(request, 'search/search_stock.html',{ 'ViewVendor':results, 'ViewStock':viewstock })





@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def PrintSearchedStock(request):
        
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = r.cursor()
    # vendor_id = request.POST.get('vendor_id')
    print("....Print Vendor Id - ", vendor_id)
    
    if vendor_id != 'null':
        stock = 'select s.stock_id, p.product_name, v.vendor_name, s.quantity, s.stock_in_date, (s.quantity - s.available_stock) as total_assigned,  s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id inner join assetmanager.vendor v on v.vendor_id = p.vendor_id where v.vendor_id = '+vendor_id+' order by s.stock_id desc; '
        cursor.execute(stock)
        viewstock = tuple(cursor.fetchall())

    else:
        stock = 'select s.stock_id, p.product_name, v.vendor_name, s.quantity, s.stock_in_date, (s.quantity - s.available_stock) as total_assigned,  s.available_stock, s.added_by  from assetmanager.stock s INNER JOIN assetmanager.product p on p.product_id = s.product_id inner join assetmanager.vendor v on v.vendor_id = p.vendor_id where v.vendor_id != " "  order by s.stock_id desc; '
        cursor.execute(stock)
        viewstock = tuple(cursor.fetchall())
    # lst = {'employee_id':employee_id, 'department_id':department_id, 
    # 'product_id':product_id, 'status':status, 'office_location_id':office_location_id, 'assign_date':assign_date, 
    # 'fromdate':fromdate, 'todate':todate}

    today = date.today()
    dateformate = today.strftime("%B %d, %Y")
    # print("....... today = ", dateformate)

    currtime = datetime.now()
    timeformat = currtime.strftime("%I:%M %p")
    # print("....... Time = ", timeformat)

    return render(request, 'pdf/print_stock_report.html',{'PrintStock':viewstock, "DATE":dateformate, "TIME":timeformat})
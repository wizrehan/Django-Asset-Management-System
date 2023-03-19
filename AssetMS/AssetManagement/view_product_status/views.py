from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.


def ViewProductStatus(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_product_status.html', {'ViewProdStatus':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteProductStatus(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.product_status ps set ps.is_deleted = 'YES', ps.delete_edited_by = %(delete_edited_by)s  where product_status_id = %(product_status_id)s"

    lst = {'delete_edited_by':user,'product_status_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst)   
    m.commit()
    messages.error(request, "Product Status Deleted !")
    
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_product_status.html', {'ViewProdStatus':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditProductStatus(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getuser = user
        getstatusid = id
        getstatus = request.POST.get('status')
        
        

        print("-----Details - ", getstatusid, getstatus, getuser)
 
        editmanufacturer = 'update assetmanager.product_status ps set ps.status = "'+getstatus+'" , ps.delete_edited_by = "'+getuser+'" where ps.product_status_id = "'+getstatusid+'"'
        cursor.execute(editmanufacturer) 
        m.commit()
        messages.success(request, "Product Status Updated!")

        c = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

        return render(request, 'view/view_product_status.html', {'ViewProdStatus':results})
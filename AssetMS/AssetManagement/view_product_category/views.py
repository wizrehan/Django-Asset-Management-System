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


def ViewProductCategory(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_product_category.html', {'ViewCategory':results})



@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteProductCategory(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.product_category pc set pc.is_deleted = 'YES', pc.delete_edited_by = %(delete_edited_by)s  where category_id = %(category_id)s"

    lst = {'delete_edited_by':user,'category_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst)  
    m.commit()

    messages.error(request, "Product Category Deleted !")
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_product_category.html', {'ViewCategory':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditProductCategory(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getuser = user
        getcategoryid = id
        getcategoryname = request.POST.get('category_name')
        
        

        print("-----Details - ", getcategoryid, getcategoryname, getuser)
 
        editmanufacturer = 'update assetmanager.product_category pc set pc.category_name = "'+getcategoryname+'" , pc.delete_edited_by = "'+getuser+'" where pc.category_id = "'+getcategoryid+'"'
        cursor.execute(editmanufacturer) 
        m.commit()
        messages.success(request, "Product Category Updated!")

        c = "SELECT * FROM assetmanager.product_category pc where pc.is_deleted != 'YES' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

        return render(request, 'view/view_product_category.html', {'ViewCategory':results})
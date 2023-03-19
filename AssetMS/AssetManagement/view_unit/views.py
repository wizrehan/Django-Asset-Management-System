from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import Unit
from django.contrib import messages 

m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
cursor = m.cursor()

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
  

def ViewUnit(request):
    
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_unit.html', {'ViewUnit':results})


 
# def ViewCRUD(request):
    
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     c = "SELECT * FROM assetmanager.unit"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())
#     return render(request, 'view/crud.html', {'ViewUni_':results})


# def DeleteUnit(request,id):
#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     c = 'Delete from assetmanager.unit where unit_id =  %(unit_id)s'
    
#     # tup = list[id]
#     lst = {'unit_id':id}
#     print("passing ID = ", id)
#     cursor.execute(c,lst)
#     m.commit()

    
#     cursor = m.cursor()
#     c = "SELECT * FROM assetmanager.unit"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())

#     return render(request, 'view/view_unit.html', {'ViewUnit':results})


 
@ login_required(login_url='/')
@allowed_user(['admin']) 
def DeleteUnitCopy(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.unit u set u.is_deleted = 'YES', u.delete_edited_by = %(delete_edited_by)s  where unit_id = %(unit_id)s"

    lst = {'delete_edited_by':user,'unit_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()
 
    messages.error(request, "Unit Deleted!")
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_unit.html', {'ViewUnit':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditUnit(request, id): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getunitid = id
        getunitname = request.POST.get('unit_name')
        

        print("-----Details - ", getunitid, getunitname)
 
        editunit = 'update assetmanager.unit u set u.unit_name = "'+getunitname+'" where u.unit_id= "'+getunitid+'"'
        cursor.execute(editunit) 
        m.commit()
        messages.success(request, "Unit Updated!")

        c = "SELECT * FROM assetmanager.unit des where des.is_deleted != 'YES'"
        cursor.execute(c)
        results = tuple(cursor.fetchall())


        return render(request, 'view/view_unit.html', {'ViewUnit':results})
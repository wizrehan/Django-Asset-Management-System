from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewDep
from django.contrib import messages 

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

# Create your views here.
def ViewDepartment(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_department.html', {'ViewDep':results})




# def DeleteDepartment(request,id):

#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     d = 'Delete from assetmanager.department where department_id =  %(department_id)s'
#     # tup = list[id]
#     lst = {'department_id':id}
#     print("passing ID = ", id)
#     cursor.execute(d,lst)
#     m.commit() 

    
#     c = "SELECT * FROM assetmanager.department"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())
#     return render(request, 'view/view_department.html', {'ViewDep':results})


@ login_required(login_url='/')
@allowed_user(['admin'])

def DeleteDepartment(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.department d set d.is_deleted = 'YES', d.delete_edited_by = %(delete_edited_by)s  where department_id = %(department_id)s"

    lst = {'delete_edited_by':user,'department_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Department Deleted!")
    
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_department.html', {'ViewDep':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditDepartment(request, id):

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getdepartmentid = id
        getdepartmentname = request.POST.get('department_name')
        

        print("-----Details - ", getdepartmentid, getdepartmentname)
 
        editdepartment = 'update assetmanager.department d set d.department_name = "'+getdepartmentname+'" where d.department_id= "'+getdepartmentid+'"'
        cursor.execute(editdepartment) 
        m.commit()
        messages.success(request, "Department Updated!")

        c = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
        cursor.execute(c)
        results = tuple(cursor.fetchall())


        return render(request, 'view/view_department.html', {'ViewDep':results})
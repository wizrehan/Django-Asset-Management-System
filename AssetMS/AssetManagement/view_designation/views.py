from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewDes
from django.contrib import messages 


from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.

def ViewDesignation(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.designation des where des.is_deleted != 'YES'"
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_designation.html', {'ViewDes':results})



# def DeleteDesignation(request,id):

#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     d = 'Delete from assetmanager.designation where designation_id =  %(designation_id)s'
#     # tup = list[id]
#     lst = {'designation_id':id}
#     print("passing ID = ", id)
#     cursor.execute(d,lst)
#     m.commit()

#     c = "SELECT * FROM assetmanager.designation"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())
#     return render(request, 'view/view_designation.html', {'ViewDes':results})

@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteDesignation(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.designation des set des.is_deleted = 'YES', des.delete_edited_by = %(delete_edited_by)s  where designation_id = %(designation_id)s"

    lst = {'delete_edited_by':user,'designation_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()
    messages.error(request, "Designation Deleted!")
    
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.designation des where des.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_designation.html', {'ViewDes':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditDesignation(request, id): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getdesignationid = id
        getdesignationname = request.POST.get('designation_name')
        

        print("-----Details - ", getdesignationid, getdesignationname)
 
        editdesignation = 'update assetmanager.designation des set des.designation_name = "'+getdesignationname+'" where des.designation_id= "'+getdesignationid+'"'
        cursor.execute(editdesignation) 
        m.commit()
        messages.success(request, "Designation Updated!")

        c = "SELECT * FROM assetmanager.designation des where des.is_deleted != 'YES'"
        cursor.execute(c)
        results = tuple(cursor.fetchall())


        return render(request, 'view/view_designation.html', {'ViewDes':results})
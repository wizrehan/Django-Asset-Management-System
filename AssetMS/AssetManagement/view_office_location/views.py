from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewOffice
from django.contrib import messages 

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/') 
@allowed_user(['admin', 'user'])
# Create your views here.


def ViewOfficeLocation(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.office_location ol where ol.is_deleted != 'YES'"
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_office_location.html', {'ViewOffice':results})
 



# def DeleteOfficeLocation(request,id):

#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     d = 'Delete from assetmanager.office_location where office_location_id =  %(office_location_id)s'
#     # tup = list[id]
#     lst = {'office_location_id':id}
#     print("passing ID = ", id)
#     cursor.execute(d,lst)
#     m.commit() 

    
#     c = "SELECT * FROM assetmanager.office_location"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())
#     return render(request, 'view/view_office_location.html', {'ViewOffice':results})



@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteOfficeLocation(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.office_location ol set ol.is_deleted = 'YES', ol.delete_edited_by = %(delete_edited_by)s  where office_location_id = %(office_location_id)s"

    lst = {'delete_edited_by':user,'office_location_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst)  
    m.commit()
    messages.success(request, "Office Address Deleted !")
    
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.office_location ol where ol.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_office_location.html', {'ViewOffice':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditOfficeLocation(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getuser = user
        getofficed = id
        getofficename = request.POST.get('address')
        

        print("-----Details - ", getofficed, getofficename)
 
        editoffice = 'update assetmanager.office_location ol set ol.address = "'+getofficename+'" , ol.delete_edited_by = "'+getuser+'" where ol.office_location_id = "'+getofficed+'"'
        cursor.execute(editoffice) 
        m.commit()
        messages.success(request, "Office Address Updated!")

        c = "SELECT * FROM assetmanager.office_location ol where ol.is_deleted != 'YES' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

        return render(request, 'view/view_office_location.html', {'ViewOffice':results})
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


def ViewManufacturer(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.manufacturer manu where manu.is_deleted != 'YES'"
    cursor.execute(c)
    results = tuple(cursor.fetchall())
    return render(request, 'view/view_manufacturer.html', {'ViewManufacture':results})


@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteManufacturer(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.manufacturer manu set manu.is_deleted = 'YES', manu.delete_edited_by = %(delete_edited_by)s  where manufacturer_id = %(manufacturer_id)s"

    lst = {'delete_edited_by':user,'manufacturer_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst)    
    m.commit()
    messages.error(request, "Manufacturer Deleted !")
    
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.manufacturer manu where manu.is_deleted != 'YES' "
    cursor.execute(c) 
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_manufacturer.html', {'ViewManufacture':results})





@ login_required(login_url='/')
@allowed_user(['admin'])
def EditManufacturer(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getuser = user
        getmanuid = id
        getmanuname = request.POST.get('manufacturer_name')
        getmanucountry = request.POST.get('country')
        

        print("-----Details - ", getmanuid, getmanuname, getmanucountry, getuser)
 
        editmanufacturer = 'update assetmanager.manufacturer m set m.manufacturer_name = "'+getmanuname+'" , m.country = "'+getmanucountry+'" , m.delete_edited_by = "'+getuser+'" where m.manufacturer_id = "'+getmanuid+'"'
        cursor.execute(editmanufacturer) 
        m.commit()
        messages.success(request, "Manufacturer Updated!")

        c = "SELECT * FROM assetmanager.manufacturer manu where manu.is_deleted != 'YES' "
        cursor.execute(c) 
        results = tuple(cursor.fetchall())

        return render(request, 'view/view_manufacturer.html', {'ViewManufacture':results})
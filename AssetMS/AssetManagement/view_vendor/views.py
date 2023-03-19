from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewVendor
from django.http import FileResponse
import io
from django.contrib.auth.models import Group, User
from django.contrib import messages






from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.

 
def ViewVendor(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES'"
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    

    
    
    return render(request, 'view/view_vendor.html', {'ViewVendoor':results})


# def DeleteVendor(request,id):


#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
    
#     c = ("Delete from assetmanager.vendor where vendor_id=%s",id)
#     print('Hello',c)
#     cursor.execute(c)

#     # obj= Unit.objects.get(unit_id=id)
#     # if request.method=='POST':
#     #         obj.delete()
#     # return redirect("/emp_delete/")
#     # messages.info(request, "Employee details deleted!")
#     # context={
#     #          'context_obj': obj
#     #         }
    
#     #results = tuple(cursor.fetchall())
#     return render(request, 'view/view_vendor.html')



@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteVendor(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.vendor v set v.is_deleted = 'YES', v.delete_edited_by = %(delete_edited_by)s  where vendor_id = %(vendor_id)s"

    lst = {'delete_edited_by':user,'vendor_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()

    messages.error(request, "Vendor Deleted !")
    cursor = m.cursor()
    c = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES' "
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    return render(request, 'view/view_vendor.html', {'ViewVendoor':results})




@ login_required(login_url='/')
@allowed_user(['admin'])
def EditVendor(request, id, user): 

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition") 
    if request.method == "POST": 
        getvendorid = id 
        getuser = user
        getvendorname = request.POST.get('vendor_name')
        getcontact = request.POST.get('conatct')
        getemail = request.POST.get('email')
        getlocation = request.POST.get('location')
        getcontactperson = request.POST.get('contact_person')
        gettype = request.POST.get('vendor_type')
        

        

        print("-----Details - ", getvendorid, getuser, getvendorname, getcontact, getemail, getlocation, getcontactperson, gettype) 
 
        editproduct = 'update assetmanager.vendor v set v.vendor_name = "'+getvendorname+'" , v.vendor_contact = "'+getcontact+'", v.vendor_mail = "'+getemail+'", v.vendor_location = "'+getlocation+'", v.contact_person = "'+getcontactperson+'", v.vendor_type = "'+gettype+'", v.delete_edited_by = "'+getuser+'" where v.vendor_id = "'+getvendorid+'"'
        cursor.execute(editproduct) 
        m.commit()
        messages.success(request, "Vendor Updated!")

        
        c = "SELECT * FROM assetmanager.vendor v where v.is_deleted != 'YES' "
        cursor.execute(c)
        results = tuple(cursor.fetchall())

        return render(request, 'view/view_vendor.html', {'ViewVendoor':results})
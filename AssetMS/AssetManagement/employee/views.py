from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from django.core import serializers
from .models import ViewDep, AddEmployee






employee_name = ''
department_id = ''
designation_id = ''
unit_id = ''
contact = ''
employee_mail = ''
office_location_id = ''
employee_status = ''


from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])
# Create your views here.
def add_employee(request):
    
    global employee_name, department_id, designation_id, unit_id, contact, employee_mail, office_location_id, employee_status
    
    if request.method == "POST":
        if request.POST.get('employee_id') and request.POST.get('employee_name') and request.POST.get('department_id') and request.POST.get('designation_id') and request.POST.get('unit_id') and request.POST.get('contact') and request.POST.get('employee_mail') and request.POST.get('office_location_id') and request.POST.get('employee_status') and request.POST.get('is_deleted'):
            saverecord = AddEmployee()
            saverecord.employee_id = request.POST.get('employee_id')
            saverecord.employee_name = request.POST.get('employee_name')
            saverecord.department_id = request.POST.get('department_id')
            saverecord.designation_id = request.POST.get('designation_id')
            saverecord.unit_id = request.POST.get('unit_id')
            saverecord.contact = request.POST.get('contact')
            saverecord.employee_mail = request.POST.get('employee_mail')
            saverecord.office_location_id = request.POST.get('office_location_id')
            saverecord.employee_status = request.POST.get('employee_status')
            saverecord.create_by = request.POST.get('create_by') 
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Employee Added Succesfully !")
            return render(request, 'pages/add_employee.html')
    
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    
    query = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(query)
    results = tuple(cursor.fetchall())

    query1 = "SELECT * FROM assetmanager.designation des where des.is_deleted != 'YES' "
    cursor.execute(query1) 
    results1 = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    query3 = "SELECT * FROM assetmanager.office_location"
    cursor.execute(query3)
    results3 = tuple(cursor.fetchall())

    return render(request, 'pages/add_employee.html', {'ViewDep':results, 'ViewDes':results1,'ViewUnit':results2, 'ViewOL':results3})






from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import mysql.connector as sql
from .models import ViewEmp
from employee.models import AddEmployee
from datetime import date, time, datetime
from django.contrib import messages 



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here. 


def ViewEmployee(request):
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    c = "select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id where e.is_deleted != 'YES';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())

    
    query = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(query)
    resultsdep = tuple(cursor.fetchall())

    return render(request, 'view/view_employee.html', {'ViewEmp':results, 'ViewDep':resultsdep})

  

# def DeleteEmployee(request,id):

#     lst = []
#     m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
#     cursor = m.cursor()
#     c = 'Delete from assetmanager.employee where employee_id =  %(employee_id)s'
#     # tup = list[id]
#     lst = {'employee_id':id}
#     print("passing ID = ", id)
#     cursor.execute(c,lst)
#     m.commit()

    
#     c = "select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id;"
#     cursor.execute(c)
#     results = tuple(cursor.fetchall())

#     return render(request, 'view/view_employee.html', {'ViewEmp':results})

@ login_required(login_url='/')
@allowed_user(['admin'])
def DeleteEmployee(request,user,id):
    lst = []
    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    
    isdelete = "update assetmanager.employee e set e.is_deleted = 'YES', e.delete_edited_by = %(delete_edited_by)s  where employee_id = %(employee_id)s"

    lst = {'delete_edited_by':user,'employee_id':id}
    print("passing ID = ",user, id)
    cursor.execute(isdelete,lst) 
    m.commit()

     
    cursor = m.cursor()
    c = "select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id where e.is_deleted != 'YES';"
    cursor.execute(c)
    results = tuple(cursor.fetchall())


    return render(request, 'view/view_employee.html', {'ViewEmp':results})


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])

def EditEmployee(request, id, user):

    m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
    cursor = m.cursor()
    lst = []
    print(".....BEfore IF Condition")
    if request.method == "POST": 
        getemployeeid = id
        getemployeename = request.POST.get('employee_name')
        getcontact = request.POST.get('contact')
        getmail = request.POST.get('email')
        getdepartment = request.POST.get('department_id')

        print("-----Details - ", getemployeename, getcontact, getmail, getdepartment)

        editemployee = 'update assetmanager.employee e set e.department_id = "'+getdepartment+'" ,  e.employee_name ="'+getemployeename+'" , e.contact = "'+getcontact+'" , e.employee_mail = "'+getmail+'" ,  e.delete_edited_by = %(delete_edited_by)s where e.employee_id = "'+getemployeeid+'"'
        
        lst = {'delete_edited_by':user}
        cursor.execute(editemployee,lst) 
        m.commit()
        messages.success(request, "Employee Record Updated !")

        c = "select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id where e.is_deleted != 'YES';"
        cursor.execute(c)
        results = tuple(cursor.fetchall())

       
        query = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
        cursor.execute(query)
        resultsdep = tuple(cursor.fetchall())

        return render(request, 'view/view_employee.html', {'ViewEmp':results, 'ViewDep':resultsdep})



@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def SearchEmployee(request):
    global employee_id, department_id, unit_id
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        department_id = request.POST.get('department_id') 
        unit_id = request.POST.get('unit_id')
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()

        EMP = 'select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id where e.employee_id = '+employee_id+' or dep.department_id = '+department_id+' or u.unit_id = '+unit_id+' '
        cursor.execute(EMP)
        EMPSearch = tuple(cursor.fetchall())

        
        query = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
        cursor.execute(query)
        results = tuple(cursor.fetchall()) 

        c = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES' "
        cursor.execute(c)
        unit = tuple(cursor.fetchall())
        return render(request, 'search/employee_search.html',{'SearchEmp':EMPSearch, 'ViewDep':results, 'ViewUnit': unit})
        # else:


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor() 
    query = "SELECT * FROM assetmanager.department d where d.is_deleted != 'YES'"
    cursor.execute(query)
    results = tuple(cursor.fetchall())


    c = "SELECT * FROM assetmanager.unit u where u.is_deleted != 'YES' "
    cursor.execute(c)
    unit = tuple(cursor.fetchall())

    return render(request, 'search/employee_search.html',{ 'ViewDep':results, 'ViewUnit': unit})
    


@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
def PrintSearchedEmployee(request):
    
        r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager') 
        cursor = r.cursor()
        print("..........Print Function() = ", 
        "Employee ID = ",employee_id, 
        "Department ID = ", department_id,
        "Unit ID = ", unit_id)
        

        EMP = 'select e.employee_id, e.employee_name, dep.department_name, des.designation_name, u.unit_name, e.contact, e.employee_mail, ol.address, e.employee_status from assetmanager.employee e INNER JOIN assetmanager.department dep on dep.department_id = e.department_id INNER JOIN assetmanager.designation des on des.designation_id = e.designation_id INNER JOIN assetmanager.unit u on u.unit_id = e.unit_id INNER JOIN assetmanager.office_location ol on ol.office_location_id=e.office_location_id where e.employee_id = '+employee_id+' or dep.department_id = '+department_id+' or u.unit_id = '+unit_id+' '
        cursor.execute(EMP)
        PrintEmployee = tuple(cursor.fetchall())
        # lst = {'employee_id':employee_id, 'department_id':department_id, 
        # 'product_id':product_id, 'status':status, 'office_location_id':office_location_id, 'assign_date':assign_date, 
        # 'fromdate':fromdate, 'todate':todate}

        today = date.today()
        dateformate = today.strftime("%B %d, %Y")
        # print("....... today = ", dateformate)

        currtime = datetime.now()
        timeformat = currtime.strftime("%I:%M %p")
        # print("....... Time = ", timeformat)

        return render(request, 'pdf/print_employee_report.html',{'PrintEmployee':PrintEmployee, "DATE":dateformate, "TIME":timeformat})
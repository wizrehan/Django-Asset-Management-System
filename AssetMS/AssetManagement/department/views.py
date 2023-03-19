from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddDepartment


department_name = ''

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])
# Create your views here.
def add_department(request):
    global  department_name

    if request.method == "POST":
        if request.POST.get('department_name'):
            saverecord = AddDepartment()
            saverecord.department_name = request.POST.get('department_name')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Department Added Succesfully !")
            return render(request, 'pages/add_department.html')
               

    return render(request, "pages/add_department.html")
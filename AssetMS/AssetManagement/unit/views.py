from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddUnit


unit_name = ''
unit_id = ''

m = sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
cursor = m.cursor()

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])

# Create your views here.
def add_unit(request):
    global unit_id, unit_name

    if request.method == "POST":
        if request.POST.get('unit_name'):
            saverecord = AddUnit()
            saverecord.unit_name = request.POST.get('unit_name')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Unit Added Succesfully !")
            return render(request, 'pages/add_unit.html')
              

    return render(request, "pages/add_unit.html") 






      
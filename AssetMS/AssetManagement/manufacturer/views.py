from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddManufacturer


manufacturer_name = ''
country =''

from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def add_manufacturer(request):
    global manufacturer_id, manufacturer_name, country 

    if request.method == "POST":
        if request.POST.get('manufacturer_name') and request.POST.get('country'):
            saverecord = AddManufacturer()
            saverecord.manufacturer_name = request.POST.get('manufacturer_name')
            saverecord.country = request.POST.get('country')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Manufacturer Added Succesfully !")
            return render(request, 'pages/add_manufacturer.html')
            

    return render(request, "pages/add_manufacturer.html")
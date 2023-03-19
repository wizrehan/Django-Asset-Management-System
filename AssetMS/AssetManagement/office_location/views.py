from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddOfficeLocation


address = '' 



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])
# Create your views here.
def add_office_loc(request):
    global office_loc_id, address

    if request.method == "POST":
       if request.POST.get('address'):
        saverecord = AddOfficeLocation()
        saverecord.address = request.POST.get('address')
        saverecord.added_by = request.POST.get('added_by')
        saverecord.is_deleted = request.POST.get('is_deleted')
        saverecord.save()
        messages.success(request, "Office Location  Added Succesfully !")
        return render(request, 'pages/add_office_loc.html')
              

    return render(request, "pages/add_office_loc.html")
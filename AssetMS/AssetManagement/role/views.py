from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from .models import RoleInsert
from django.contrib import messages


role_name = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])
# Create your views here.
def create_role(request):

    if request.method == "POST":
        if request.POST.get('role_name'):
            saverecord = RoleInsert()
            saverecord.role_name = request.POST.get('role_name')
            saverecord.save()
            messages.success(request, 'Role Created Succesfully !')
            return render(request, 'pages/create_role.html')
    
              

    return render(request, "pages/create_role.html")
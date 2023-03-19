from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
import mysql.connector as sql
from .models import CreateUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreation

username = ''
full_name = ''
password = ''
contact = ''
mail = ''
role_id = ''
status = ''

# Create your views here.
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])

def create_user(request):
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    employee_id = request.POST.get('employee_id')
    
    form = UserCreation()
    
    print("------ Emoloyee Id = ", employee_id)
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            
            form.save()
            user = form.cleaned_data.get('username')
            cursor.execute('update assetmanager.auth_user au set au.employee_id = "'+employee_id+'" where au.username = "'+user+'" ')
            r.commit()
            print("____ Employee ID Saved")
            
            
            messages.success(request, 'Account created for' + ' ' + user)
            return redirect('create_user')


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT * FROM assetmanager.role"
    cursor.execute(query)
    results = tuple(cursor.fetchall())


    return render(request, "pages/create_user.html",{'ViewRole':results, 'form':form})




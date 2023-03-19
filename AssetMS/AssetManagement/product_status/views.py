from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import ViewProductStatus
from django.contrib.auth.models import User  


status = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def add_product_status(request): 
    global status_name

    if request.method == "POST":
        if request.POST.get('status') and request.POST.get('added_by'):
            saverecord = ViewProductStatus()
            saverecord.status = request.POST.get('status')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Product status Added Successfully !")
            return render(request, "pages/add_product_status.html")
              
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT username FROM assetmanager.auth_user;"
    cursor.execute(query)
    results = tuple(cursor.fetchall())
    return render(request, "pages/add_product_status.html", {'Viewuser':results}) 
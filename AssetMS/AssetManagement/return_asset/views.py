from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import ReturnAsset
from django.contrib.auth.models import User  


status = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def Return_Asset(request): 
    
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    if request.method == "POST":
   
       if request.POST.get('product_id') and request.POST.get('employee_id') and request.POST.get('return_date') and request.POST.get('product_status') and request.POST.get('return_reason') and request.POST.get('comments'):
            
            
            saverecord = ReturnAsset()
            saverecord.product_id = request.POST.get('product_id')
            saverecord.employee_id = request.POST.get('employee_id')
            saverecord.return_date = request.POST.get('return_date')
            saverecord.product_status = request.POST.get('product_status')
            saverecord.return_reason = request.POST.get('return_reason')
            saverecord.comments = request.POST.get('comments')
            saverecord.received_by = request.POST.get('received_by')
            saverecord.countr = 'NO'
            saverecord.save()
            messages.success(request, "Asset Returned Succesfully !")
            return render(request, 'pages/return_asset.html')
              
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES' "
    cursor.execute(query)
    results = tuple(cursor.fetchall())

    query1 = "SELECT * FROM assetmanager.employee e where e.is_deleted != 'YES' "
    cursor.execute(query1)
    results1 = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.product_status ps where ps.is_deleted != 'YES' "
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall()) 
    
    

    

    return render(request, "pages/return_asset.html", {'ViewProduct':results, 'ViewEmp':results1, 'ViewProductStatus':results2})

    

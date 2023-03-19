from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddStock


product_id = ''
quantity = ''
stock_in_date = ''
available_stock = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin'])
# Create your views here.
def add_stock(request):
    global  product_id, quantity, stock_in_date, available_stock

    if request.method == "POST":
       if request.POST.get('product_id') and request.POST.get('quantity') and request.POST.get('stock_in_date') :
            saverecord = AddStock()
            saverecord.product_id = request.POST.get('product_id')
            saverecord.quantity = request.POST.get('quantity')
            saverecord.stock_in_date = request.POST.get('stock_in_date')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.save()
            messages.success(request, "Stock Added Succesfully !")
            return render(request, 'pages/add_stock.html')

    
    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT * FROM assetmanager.product p where p.is_deleted != 'YES' "
    cursor.execute(query)
    results = tuple(cursor.fetchall())
              

    return render(request, "pages/add_stock.html", {'ViewProduct':results})


 
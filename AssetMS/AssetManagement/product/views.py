from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddProduct


product_name = ''
manufacture_id = ''
category_id = '' 
vendor_id = ''
warranty_till = ''
serial_IMEI =''
specification = ''
invoice_no = ''
purchase_date = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def add_product(request):
    
    global  product_name, manufacture_id,category_id, vendor_id, warranty_till,serial_IMEI, specification, invoice_no, purchase_date

    if request.method == "POST":
        if request.POST.get('product_name') and request.POST.get('manufacture_id') and request.POST.get('category_id') and request.POST.get('vendor_id') and request.POST.get('warranty_till') and request.POST.get('serial_IMEI') and request.POST.get('specification') and request.POST.get('invoice_no') and request.POST.get('purchase_date') and request.POST.get('is_deleted'):
            saverecord = AddProduct()
            saverecord.product_name = request.POST.get('product_name')
            saverecord.manufacture_id = request.POST.get('manufacture_id')
            saverecord.category_id = request.POST.get('category_id')
            saverecord.vendor_id = request.POST.get('vendor_id')
            saverecord.warranty_till = request.POST.get('warranty_till')
            saverecord.serial_IMEI = request.POST.get('serial_IMEI')
            saverecord.specification = request.POST.get('specification')
            saverecord.invoice_no = request.POST.get('invoice_no')
            saverecord.purchase_date = request.POST.get('purchase_date')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Product Added Succesfully !")
            return render(request, 'pages/create_product.html')


    r= sql.connect(host='127.0.0.1', user='root', passwd = '72750', port = '3306', database = 'assetmanager')
    cursor = r.cursor()
    query = "SELECT * FROM assetmanager.manufacturer"
    cursor.execute(query)
    results = tuple(cursor.fetchall())

    query1 = "SELECT * FROM assetmanager.product_category"
    cursor.execute(query1)
    results1 = tuple(cursor.fetchall())

    query2 = "SELECT * FROM assetmanager.vendor"
    cursor.execute(query2)
    results2 = tuple(cursor.fetchall())

    return render(request, "pages/create_product.html", {'ViewManu':results, 'ViewProC':results1, 'ViewVendor':results2})
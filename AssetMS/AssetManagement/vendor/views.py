from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import AddVendor




from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def add_vendor(request): 
    
    global  vendor_name, vendor_contact, vendor_mail, vendor_location, contact_person, vendor_type, vendor_status, has_trade, trade_document
    print("...... Before IF")
    if request.method == "POST":
       if request.POST.get('vendor_name') and request.POST.get('vendor_contact') and request.POST.get('vendor_mail') and request.POST.get('vendor_location') and request.POST.get('contact_person') and request.POST.get('vendor_type') and request.POST.get('vendor_status') and request.POST.get('has_trade') and request.POST.get('trade_document'):
            saverecord = AddVendor()
            saverecord.vendor_name = request.POST.get('vendor_name')
            saverecord.vendor_contact = request.POST.get('vendor_contact')
            saverecord.vendor_mail = request.POST.get('vendor_mail')
            saverecord.vendor_location = request.POST.get('vendor_location')
            saverecord.contact_person = request.POST.get('contact_person')
            saverecord.vendor_type = request.POST.get('vendor_type')
            saverecord.vendor_status = request.POST.get('vendor_status')
            saverecord.has_trade = request.POST.get('has_trade')
            saverecord.trade_document = request.POST.get('trade_document')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            print("...... After IF")
            saverecord.save()
            print("...... After Save IF")
            messages.success(request, "Vendor Added Succesfully !")
            return render(request, 'pages/add_vendor.html')


    return render(request, "pages/add_vendor.html")
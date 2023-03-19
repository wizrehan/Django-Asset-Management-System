from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib import messages
from .models import ViewProductCategory


category_name = ''



from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_user
@ login_required(login_url='/')
@allowed_user(['admin', 'user'])
# Create your views here.
def add_product_category(request):
    global category_id, category_name

    if request.method == "POST":
        if request.POST.get('category_name'):
            saverecord = ViewProductCategory()
            saverecord.category_name = request.POST.get('category_name')
            saverecord.added_by = request.POST.get('added_by')
            saverecord.is_deleted = request.POST.get('is_deleted')
            saverecord.save()
            messages.success(request, "Product Category Added Successfully !")
            return render(request, "pages/add_product_category.html")
              

    return render(request, "pages/add_product_category.html")
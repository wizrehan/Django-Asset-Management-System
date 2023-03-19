"""AssetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.views import login
from user.views import create_user

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('', include('dashboard.urls')),
    path('', include('user.urls')),
    path('', include('product.urls')),
    path('', include('role.urls')),
    path('', include('stock.urls')),
    path('', include('office_location.urls')),
    path('', include('department.urls')),
    path('', include('designation.urls')),
    path('', include('unit.urls')),
    path('', include('manufacturer.urls')),
    path('', include('product_category.urls')),
    path('', include('vendor.urls')),
    path('', include('employee.urls')),
    path('', include('assign_asset.urls')),
    path('', include('view_employee.urls')),
    path('', include('view_department.urls')),
    path('', include('view_designation.urls')), 
    path('', include('view_unit.urls')),
    path('', include('view_office_location.urls')),
    path('', include('view_product.urls')),
    path('', include('view_stock.urls')),
    path('', include('view_vendor.urls')),
    path('', include('view_manufacturer.urls')),
    path('', include('view_product_category.urls')),
    path('', include('product_status.urls')),
    path('', include('view_product_status.urls')),
    path('', include('return_asset.urls')),
    path('', include('view_return_asset.urls')),
    path('', include('Product_Requisition.urls')),
    
]

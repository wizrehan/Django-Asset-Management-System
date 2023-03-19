from django.urls import path

from . import views

urlpatterns = [

    path('add_vendor/',views.add_vendor, name='add_vendor'),
    
]
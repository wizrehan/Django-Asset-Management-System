from django.urls import path

from . import views

urlpatterns = [

    path('create_role/',views.create_role, name='create_role')
    
]
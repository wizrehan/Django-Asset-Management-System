from django.urls import path

from . import views

urlpatterns = [

    path('view_vendor/',views.ViewVendor, name='view_vendor'),
    path('delete_vendor/<user>/<id>', views.DeleteVendor, name='deletevendor'),
    path('edit_vendor/<id>/<user>', views.EditVendor,name='edit_vendor'), 
    # path('vendor_pdf/', views.MyPDFView.as_view(), name='generatevendorreport')
    
]
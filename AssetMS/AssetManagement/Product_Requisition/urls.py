from django.urls import path

from . import views
 
urlpatterns = [ 

    path('View_product_list/<user>',views.GETProduct, name='view_product_list'),
    path('make_requisition/<user>', views.MakeRequisition, name='makerequisition'),
    path('view_requested_asset/', views.ViewRequestedAsset, name='viewrequestedasset'),
    path('accept_request/<id>/<user>', views.AcceptRequisition, name='acceptrequest'),
    path('reject_request/<id>/<user>', views.RejectRequisition, name='rejectrequest'),
    path('view_user_request/<user>', views.ViewDepartmentRequest, name='viewuserrequest'),
    path('make_requisition_test/<user>', views.MakeRequisitionTEST, name='makerequisition_test'),
    path('View_product_list_test/<user>',views.GETProductTEST, name='view_product_list_test'),


    
]
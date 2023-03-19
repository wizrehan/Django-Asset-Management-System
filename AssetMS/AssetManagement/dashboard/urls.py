from django.urls import path

from . import views


 
urlpatterns = [

    path('home/',views.home1, name='home'),
    path('', views.create_user1, name='create_user'),
    path('',views.add_department1, name='add_department'),
    path('',views.add_designation1, name='add_designation'),
    path('',views.add_employee1, name='employee'),
    path('',views.add_manufacturer1, name='manufacturer'),
    path('',views.add_office_loc1, name='add_office'),
    path('',views.add_product1, name='add_product'),
    path('',views.add_product_category1, name='product_category'),
    path('',views.create_role1, name='create_role'),
    path('',views.add_stock1, name='add_stock'),
    path('',views.add_unit1, name='add_unit'),
    path('', views.assign_asset1, name = "assign_asset"),
    path('add_vendor',views.add_vendor1, name ='add_vendor'),
    path('', views.view_employee1, name = 'view_employee'),
    path('', views.view_department1, name = 'view_department'),
    path('', views.view_designation1, name="view_designation"), 
    path('', views.view_unit1, name = 'view_unit'),
    path('', views.view_office_location1, name = 'view_office_location'), 
    path('', views.view_product1, name = 'view_product'),
    path('', views.view_stock1, name = 'view_stock'),
    path('', views.view_vendor1, name = 'view_vendor'),
    path('', views.view_manufacturer1, name= 'view_manufacturer'), 
    path('', views.view_product_category1, name='view_product_category'),
    path('', views.add_product_status1, name = 'add_product_status' ), 
    path('', views.view_product_status1, name = 'view_product_status' ),
    path('assigned_asset/',views.assigned_asset1, name='assigned_asset'),
    path('assigned_asset_delete/<id>', views.DeleteAssignedAsset, name='deleteassignedasset'),
    path('delete_brand_new_asset/<id>', views.DeleteBrandNewAsset, name='deletebrandnewasset'),
    path('delete_repaired_asset/<id>', views.DeleteRepairedAsset, name='deleterepairedasset'),
    path('delete_reused_asset/<id>', views.DeleteReUsedAsset, name='deletereusedasset'),
    path('delete_used_asset/<id>', views.DeleteUsedAsset, name='deleteusedasset'),
    path('edit_assigned_asset/<id>/<user>', views.EditAssignAsset, name = 'editassginedasset' ),
    path('edit_used_asset/<id>/<user>', views.EditUsedAsset, name = 'editusedasset' ),
    path('edit_reused_asset/<id>/<user>', views.EditReUsedAsset, name = 'editreusedasset' ),
    path('edit_repaired_asset/<id>/<user>', views.EditRepairedAsset, name = 'editrepairedasset' ),
    path('edit_barnd_new_asset/<id>/<user>', views.EditBrandNewAsset, name = 'editbrandnewasset' ),

    # path('', views.delete_items, name = 'delete'),
    # path('', views.Edit1, name='edit'),
    path('reused_asset/', views.ReUsedAsset, name='reused_asset'),
    path('used_asset/', views.UsedAsset, name='used_asset'),
    path('damaged_asset/', views.DamagedAsset, name='damaged_asset'),
    path('repaired_asset/', views.RepairedAsset, name='repaired_asset'),
    path('brand_new_asset/', views.BrandNewAsset, name='brandnew_asset'),
    path('test/',views.test, name='test'),
    
]  
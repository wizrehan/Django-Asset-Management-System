from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [  

    path('',auth_views.LoginView.as_view(template_name = 'pages/login.html'), name='login'),

    path('logout', auth_views.LogoutView.as_view(), name = 'logout' ),

    path('forgot_pass/', views.Forgot_Password, name = 'forgot_password'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
         
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),
         name='password_reset_complete'),
    
]  
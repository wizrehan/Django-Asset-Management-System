from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector as sql
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User  
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import views as auth_views
from django.conf import settings


 


# Create your views here.
def login(request):


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Succesfull !')

            for i in request.user.groups.all():
                print("---------",i.name)
                Group = i.name
            return redirect('home',{'group':Group}) 
            
        else:
            messages.success(request, 'User mail or Password is incorrect !')
            return render(request, "pages/login.html")
    
    return render(request, "pages/login.html")





def Forgot_Password(request):
    if request.method == 'POST':
        
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email = data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Request'
                    email_template_name = 'login/password_message.txt'
                    parameters = {
                        'email' : user.email,
                        'domain' : '127.0.0.1:8000',
                        'site_name' : 'BGI',
                        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                        'user' : user,
                        'token' : default_token_generator.make_token(user),
                        'protocol' : 'http',
 
                    } 
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False )
                    except BadHeaderError:
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm()
           
    return render (request, "login/forgot_password.html",context = {'password_form' : password_form} )

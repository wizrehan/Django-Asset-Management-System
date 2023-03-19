from django.http import HttpResponse

def allowed_user(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            
            else:
                return HttpResponse("You are not authorize to perform this action")
        return wrapper_func
    return decorator
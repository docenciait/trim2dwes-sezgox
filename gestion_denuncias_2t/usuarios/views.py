from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'GET':
        return render(request, 'accounts/registro.html')
    else:
        if(request.POST['password'] != request.POST['confirm']):
            return render(request, 'accounts/registro.html')
        user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
        return redirect('login')

def login(request):
    if(request.method == "GET"):
        return render(request,'accounts/login.html')
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'accounts/login.html')
        else:
            auth_login(request, user)
            return redirect('home')

@login_required
def index(request):
    return render(request, 'accounts/home.html')
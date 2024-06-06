# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'alcoholic_app/signup.html', {'error': 'password must match.'})
    return render(request, 'alcoholic_app/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home') # return redirect('board')
        else:
            return render(request, 'alcoholic_app/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'alcoholic_app/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'alcoholic_app/home.html')
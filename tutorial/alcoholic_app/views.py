# accounts/views.py
import csv
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
            return redirect('/main/home/')
        return render(request, 'templates/signup.html', {'error': 'password must match.'})
    return render(request, 'templates/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home') # return redirect('board')
        else:
            return render(request, 'teamplates/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'templates/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'templates/main.html')

def list(request):
    return render(request, 'templates/list.html')

def category_beer(request):
    return render(request, 'templates/category_beer.html')

def beer_list(request):
    return render(request, 'templates/list_beer.html')

def beer_detail(request):
    return render(request, 'templates/beer_detail.html') # ddddddd

def csv_view(request):
    data = []
    beer_name = None
    beer_description = None
    beer_img_url = None
    beer_country = None

    file_path = 'alcoholic_app/data/beer.csv'

    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            if i == 2:  # 3번째 행 (0-based 인덱스)
                beer_name = row[0]
                beer_country = row[3]
                beer_description = row[4]
                beer_img_url = row[1]
                break  # 필요한 데이터를 얻었으므로 루프를 종료

    specific_data = {
        'beer_name': beer_name,
        'beer_country': beer_country,
        'beer_description': beer_description,
        'beer_img_url': beer_img_url,
    }

    return render(request, 'templates/beer_detail.html', {'specific_data': specific_data})
# accounts/views.py
import csv
import pandas as pd
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

# def category_beer(request):
#     return render(request, 'templates/category_beer.html')

# def beer_list(request):
#     return render(request, 'templates/list_beer.html')

def beer_detail(request):
    return render(request, 'templates/beer_detail.html') # ddddddd

def test(request):
    return render(request, 'templates/rhotest.html') #dddd

def csv_view(request):
    data = []
    beer_name = None
    beer_description = None
    beer_img_url = None
    beer_country = None
    beer_score = None
    beer_category = None

    file_path = 'alcoholic_app/data/beer.csv'

    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            if i == 2:  # 3번째 행 (0-based 인덱스)
                beer_name = row[0]
                beer_country = row[3]
                beer_description = row[4]
                beer_img_url = row[1]
                beer_score = row[5]
                break  # 필요한 데이터를 얻었으므로 루프를 종료

    specific_data = {
        'beer_name': beer_name,
        'beer_country': beer_country,
        'beer_description': beer_description,
        'beer_img_url': beer_img_url,
        'beer_score': beer_score,
        'beer_category': beer_category
    }
    return render(request, 'templates/beer_detail.html', {'specific_data': specific_data})

# df = pd.read_csv('alcoholic_app/data/beer2.csv', encoding='euc-kr', index_col=0)

def csv_view_pd(request, beer_index):
    file_path = 'alcoholic_app/data/beer2.csv'
    
    # pandas를 사용하여 CSV 파일을 읽습니다.
    df = pd.read_csv(file_path, encoding='euc-kr', index_col= 0)
    
    # 특정 맥주 인덱스의 데이터를 가져옵니다.
    if beer_index < len(df):
        beer_data = df.iloc[beer_index]
        context = {
            'specific_data': {
                'beer_name': beer_data.iloc[0],  # 첫 번째 열의 데이터를 'beer_name'으로 사용
                'beer_country': beer_data.iloc[4],  # 네 번째 열의 데이터를 'beer_country'로 사용
                'beer_description': beer_data.iloc[5],  # 다섯 번째 열의 데이터를 'beer_description'으로 사용
                'beer_img_url': beer_data.iloc[1],  # 두 번째 열의 데이터를 'beer_img_url'로 사용
                'beer_score': beer_data.iloc[6],
                'beer_category': beer_data.iloc[11],
            }
        }
    else:
        context = {
            'error': '해당 인덱스의 맥주를 찾을 수 없습니다.'
        }
    
    return render(request, 'templates/beer_detail.html', context)


def category_beer(request):
    file_path = 'alcoholic_app/data/beer2.csv'
    df = pd.read_csv(file_path, encoding='euc-kr', index_col= 0) # CSV 파일을 읽어 데이터프레임으로 변환
    categories = df.iloc[:, 11].unique()  # iloc[11] 열의 유일한 카테고리 목록 가져오기
    return render(request, 'templates/beer_list_test.html', {'categories': categories})

#plz plz plz
def beer_list(request, category):
    file_path = 'alcoholic_app/data/beer2.csv'
    df = pd.read_csv(file_path, encoding='euc-kr', index_col= 0) # CSV 파일을 읽어 데이터프레임으로 변환
    filtered_df = df[df.iloc[:, 11] == category]  # iloc[11] 열에서 선택한 카테고리로 필터링
    beer_list = filtered_df.sort_values(by=df.columns[0]).to_dict(orient='records')  # 첫 번째 열로 정렬

    for beer in beer_list:
        beer['beer_name'] = beer[df.columns[0]]
        beer['beer_img_url'] = beer[df.columns[1]]
    context = {
        'category': category,
        'beer_list': beer_list
    }
    return render(request, 'templates/beers_by_category.html', context)



# def beer_list(request):
#     # categories = df.iloc[:, 11].unique()  # iloc[11] 열의 유일한 카테고리 목록 가져오기
#     return render(request, 'beer_list.html', {'categories': categories})
    
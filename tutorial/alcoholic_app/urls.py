# alcoholic_app/urls.py
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('home/list/', list, name='list'),
    path('home/beer/', category_beer, name='category_beer'),
    path('home/beer/list/<str:category>/', beer_list, name='beer_list'),
    path('home/beer/list/<int:beer_index>', views.csv_view_pd, name='csv_view'), #dddd
    # path('home/beer/list/<int:beer_index>', views.csv_view_pd, name='test'),
    # path('beers/category/<str:category>/', views.beers_by_category, name='beers_by_category'),
    # path('beers/', views.beer_list, name='beer_list'),
    # path('home/whiskey_detail',whiskey_detail, name='whiskey_detail'),  #위스키 페이지 주석
]
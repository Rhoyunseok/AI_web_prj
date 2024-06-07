# alcoholic_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('home/list/', list, name='list'),
    path('home/beer/', category_beer, name='category_beer'),
    path('home/beer/list', beer_list, name='beer_list'),
]
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
    path('home/beer/<str:category>/', beer_list, name='beer_list'),
    path('home/beer/list/<int:beer_index>', views.csv_view_pd, name='csv_view_pd'), #dddd
]
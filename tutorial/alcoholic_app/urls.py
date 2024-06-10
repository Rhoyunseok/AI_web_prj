# alcoholic_app/urls.py
from django.urls import path
from .views import *
from . import views
from .views import search_view

urlpatterns = [
    path('home/', home, name='home'),
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/beer/', category_beer, name='category_beer'),
    path('home/beer/list/<str:category>/', list_beer, name='list_beer'),
    path('home/beer/list/<int:beer_index>', views.csv_view_beer, name='csv_view_beer'), #dddd
    path('home/cocktail/', category_cocktail, name='category_cocktail'),
    path('home/cocktail/list/<str:category>/', list_cocktail, name='list_cocktail'),
    path('home/cocktail/list/<int:cocktail_index>', views.csv_view_cocktail, name='csv_view_cocktail'),
    path('home/custom/list/', list_custom, name='list_custom'),
    path('home/custom/list/<int:custom_index>', views.csv_view_custom, name='csv_view_custom'),
    path('home/wine/', category_wine, name='category_wine'),
    path('home/wine/list/<str:category>/', list_wine, name='list_wine'),
    path('home/wine/list/<int:wine_index>', views.csv_view_wine, name='csv_view_wine'),
    path('home/liquor/', category_liquor, name='category_liquor'),
    path('home/liquor/list/<str:category>/', list_liquor, name='list_liquor'),
    path('home/liquor/list/<int:liquor_index>', views.csv_view_liquor, name='csv_view_liquor'),
    path('home/whisky/', category_whisky, name='category_whisky'),
    path('home/whisky/list/<str:category>/', list_whisky, name='list_whisky'),
    path('home/whisky/list/<int:whisky_index>', views.csv_view_whisky, name='csv_view_whisky'),
    path('home/search/', search_view, name='search_view'),
]
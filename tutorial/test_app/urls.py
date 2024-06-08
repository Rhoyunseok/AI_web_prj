# test_app/urls.py

from django.urls import path
from .views import show_drink_images

urlpatterns = [
    path('drink_images/', show_drink_images, name='drink_images'),
]

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listing, name='listing'),
    path('detail', views.detail, name='detail'),
]
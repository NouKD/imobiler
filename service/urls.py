from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listing, name='listing'),
    path('<str:filtre>/<int:filtre_id>/', views.listing, name='listing'),
    path('<int:propriete_id>/detail/', views.detail, name='detail'),
    path('ajout', views.ajout, name='ajout'),
    path('search/', views.search, name='search'),
]
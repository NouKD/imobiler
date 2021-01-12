from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from . import views
from django.utils.translation import gettext_lazy as _



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('newsletter', views.newsletter, name='newsletter'),
]
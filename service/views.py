from django.shortcuts import render
from .models import *

# Create your views here.

def listing(request):
    propriete = Propriete.objects.all().order_by('-date_update')[:6]

    datas = {
        'proprietes' : propriete,
    }
    return render(request, 'pages/listing.html', datas)


def detail(request):
    datas = {

    }
    return render(request, 'pages/details.html', datas)

def ajout(request):
    datas = {

    }
    return render(request, 'pages/ajouter.html', datas)      
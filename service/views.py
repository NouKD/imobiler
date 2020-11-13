from django.shortcuts import render

# Create your views here.

def listing(request):
    datas = {

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
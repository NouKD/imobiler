from django.shortcuts import render

# Create your views here.

def listing(request):
    datas = {

    }
    return render(request, 'pages/listing.html', datas)


def detail(request):
    datas = {

    }
    return render(request, 'pages/detail.html', datas)  
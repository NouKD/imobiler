from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

def listing(request, filtre=None, filtre_id=None):
    propriete = Propriete.objects.all().order_by('-date_update')

    if filtre == 'types':
        propriete_all = propriete.filter(types=filtre_id)
    elif filtre == 'agent':
        propriete_all = propriete.filter(agent_id=filtre_id)
    else:
        propriete_all = propriete

    _paginator = Paginator(propriete_all, 4)
    page = request.GET.get('page')

    types = Types.objects.filter(status=True)
    agent = Agent.objects.filter(status=True)

    try:
        propriete_page = _paginator.page(page)
    except PageNotAnInteger:
        propriete_page = _paginator.page(1)
    except EmptyPage:
        propriete_page = _paginator.page(_paginator.num_pages)

    datas = {
        'propriete' : propriete_page,
        'propriete_recent': propriete[:6],
        'types' : types,
        'agent': agent,
    }
    return render(request, 'pages/listing.html', datas)


def detail(request,  propriete_id):
    propriete = get_object_or_404(Propriete, status=True, pk=propriete_id)
    propriete_recent = Propriete.objects.filter(status=True).order_by('-date_update')[:4]

    datas = {
        'l_propriete': propriete,
        'next_propriete': propriete.get_previous_by_date_update,
        'prev_propriete': propriete.get_next_by_date_update,
        'propriete_recent': propriete_recent,
    }

    return render(request, 'pages/details.html', datas)

def ajout(request):
    datas = {

    }
    return render(request, 'pages/ajouter.html', datas)

def search(request):
    try:
        request.POST['search']
        assert len(request.POST['search']) >= 2
    except Exception:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    q = request.POST['search']
    propriete = Propriete.objects.filter(status=True)
    propriete = propriete.filter(Q(titre__icontains=q) | Q(description__icontains=q) | Q(contenu__icontains=q))

    data = {
        'q': q,
        'propriete': propriete,
        'nombre_resultat': len(propriete),
    }

    return render(request, 'pages/search.html', data)    
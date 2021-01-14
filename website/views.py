from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from .models import Presentation, Contact, SiteInfo, SocialAccount, NewsLetter, Emplacement, Traduction, TraductionTranslation
from service.models import Propriete, Services, Agent
from .forms import ContactForm
from parler.utils.context import switch_language
# Create your views here.
def index(request):
    propriete = Propriete.objects.filter(status=True)[:6]
    position = Emplacement.objects.filter(status=True)[:8]
    presentation = Presentation.objects.filter(status=True).last
    social = SocialAccount.objects.filter(status=True)[:4]
    langue = Traduction.objects.translated('fr').order_by('translations__title')
    object_list = TraductionTranslation.objects.prefetch_related('translations')
    #for obj in object_list:
    #    print (obj.title)
    
    datas = {
        'propriete' : propriete,
        'position' : position,
        'presentation' : presentation,
        'social' : social,
        'langue' : langue,
        'object_list': object_list,
    }
    return render(request, 'pages/index.html', datas)


def about(request):
    presentation = Presentation.objects.filter(status=True).last
    propriete = Propriete.objects.filter(status=True)[:4]
    agent = Agent.objects.filter(status=True)[:4]
    social = SocialAccount.objects.filter(status=True)[:4]
    
    datas = {
       'presentation' : presentation,
       'propriete' : propriete,
       'agent' : agent,
       'social' : social,
    }
    return render(request, 'pages/about.html', datas)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    site_info = SiteInfo.objects.filter(status=True).last
    social = SocialAccount.objects.filter(status=True)[:4]

    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    
    datas = {
        'site_info' : site_info,
        'contact_form': contact_form,
        'social' : social,
    }
    return render(request, 'pages/contact.html', datas)  

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            new_email = NewsLetter.objects.create(email=email)
            new_email.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
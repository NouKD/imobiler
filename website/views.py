from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from .models import Presentation, Contact, SiteInfo, SocialAccount, NewsLetter
from service.models import Propriete, Services, Agent
from .forms import ContactForm
# Create your views here.
def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)


def about(request):
    presentation = Presentation.objects.filter(status=True).last
    propriete = Propriete.objects.filter(status=True)[:4]
    agent = Agent.objects.filter(status=True)[:4]
    
    datas = {
       'presentation' : presentation,
       'propriete' : propriete,
       'agent' : agent,
    }
    return render(request, 'pages/about.html', datas)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    site_info = SiteInfo.objects.filter(status=True).last
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    
    datas = {
        'site_info' : site_info,
        'contact_form': contact_form,
    }
    return render(request, 'pages/contact.html', datas)  

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(email=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))        
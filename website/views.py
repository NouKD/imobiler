from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from .models import Presentation, Contact, SiteInfo, SocialAccount, NewsLetter
from service.models import Propriete, Services
# Create your views here.
def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)


def about(request):
    presentation = Presentation.objects.filter(status=True).last
    propriete = Propriete.objects.filter(status=True)[:4]
    
    datas = {
       'presentation' : presentation,
       'propriete' : propriete,
    }
    return render(request, 'pages/about.html', datas)

def contact(request):
    site_info = SiteInfo.objects.filter(status=True).last
    contacter_nous = Contact.objects.filter(status=True).last
    message = ""
    if request.method == 'POST':
        nom = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            isemail = validate_email(email)
            if isemail and not email.isspace() and nom and message:
                print("1")
                contact = models.Contact(
                    nom = nom,
                    email = email,
                    sujet = sujet,
                    message = message
                )
                contact.save()
                print("3")
                message = "vous avez été enregistré"
        except :
            message = "email incorrect"
            print("2")

    datas = {
        'site_info' : site_info,
        'contacter_nous' : contacter_nous,
        'message' : message,
    }
    return render(request, 'pages/contact.html', datas)  

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(email=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))        
from django.db import models
from parler.models import TranslatableModel, TranslatedFieldsModel, TranslatedField

# Create your models here.

class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/Presentation")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom


class SocialAccount(models.Model):
    ICONS = [
        ("fa-facebook-f", "facebook"),
        ("fa-instagram", "instagram"),
        ("fa-google-plus-g", "google-plus"),
        ("fa-linkedin-in", "linkedin")
    ]

    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom



class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/SiteInfo")
    adresse = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Site info'
        verbose_name_plural = 'Site infos'

    def __str__(self):
        return self.email

class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255, null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom

class Emplacement(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:

        verbose_name = 'Emplacement'
        verbose_name_plural = 'Emplacements'

    def __str__(self):
        return self.nom

class NewsLetter(models.Model):
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'

    def __str__(self):
        return self.email


class Traduction(TranslatableModel):
    title = TranslatedField(any_language=True,)
    slug = TranslatedField()
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    
    class Meta():
        verbose_name = 'Traduction'
        verbose_name_plural = 'Traductions'
        
    def __unicode__(self):
        return self.title
    
class TraductionTranslation(TranslatedFieldsModel):
    
    master = models.ForeignKey(Traduction, related_name='translations', null=True, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=200, null=True)
    slug = models.SlugField("Slug", null=True)
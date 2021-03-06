from django.db import models

# Create your models here.


class Agent(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField()
    fonction = models.CharField(max_length=255)
    description =  models.TextField()
    tel = models.CharField(max_length=40)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:

        verbose_name = 'Agents'
        verbose_name_plural = 'Agents'

    def __str__(self):
        return self.nom

class Services(models.Model):
    nom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    description =  models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom

class Types(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:

        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.nom

class CatProjet(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/CatProjet")
    description =  models.TextField()


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'CatProjet'
        verbose_name_plural = 'CatProjets'

    def __str__(self):
        return self.nom


class Projet(models.Model):

    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Services")
    description =  models.TextField()
    cat_projet = models.ForeignKey(CatProjet, on_delete=models.CASCADE, related_name='Catprojet', null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.nom



class Propriete(models.Model):

    nom = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    commentaire = models.TextField()
    types = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='Type', null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='Agent', null=True, blank=True)
    image1 = models.ImageField(upload_to='images/Propriete')
    image2 = models.ImageField(upload_to='images/Propriete')
    image3 = models.ImageField(upload_to='images/Propriete')
    ville = models.CharField(max_length=255)
    prix = models.FloatField(null=True)
    quartier = models.CharField(max_length=255)
    situation = models.CharField(max_length=255)
    superficie = models.FloatField(null=True)
    douche = models.IntegerField(null=True)
    chambre = models.IntegerField(null=True)
    garage = models.BooleanField(default=False)
    statu = models.CharField(max_length=20) 


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'Propriete'
        verbose_name_plural = 'Proprietes'

    def __str__(self):
        return self.titre

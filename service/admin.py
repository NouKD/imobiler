from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions.action import Action

# Register your models here.

class AgentAdmin(Action):
    list_display = ('images_view', 'nom', 'fonction', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info', {'fields': ['nom', 'description', 'fonction', 'tel', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:60px; width:50px">'.format(url=obj.image.url))




class ServicesAdmin(Action):
    list_display = ('nom', 'fonction', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info', {'fields': ['nom', 'description', 'fonction']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class ProprieteAdmin(Action):
    list_display = ('images_view','superficie', 'douche', 'chambre', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info', {'fields': ['nom', 'superficie', 'douche', 'chambre', 'description', 'image1', 'image2', 'image3', 'quartier', 'situation', 'commentaire']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image1.url))


class CatProjetAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info ', {'fields': ['nom', 'image', 'description']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



class ProjetAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update','status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Projet', {'fields': ['nom', 'description', 'image', 'cat_projet']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Agent, AgentAdmin)
_register(models.Services, ServicesAdmin)
_register(models.CatProjet, CatProjetAdmin)
_register(models.Projet, ProjetAdmin)
_register(models.Propriete, ProprieteAdmin)

from django.contrib import admin

from .models import Tache

class TacheAdmin(admin.ModelAdmin):
    list_display = ('id','nom','finish','user',)
    # fields = ['nom,finish,user',]
    ordering = ('nom','user',)
    list_filter = ('user','nom')
    
admin.site.register(Tache,TacheAdmin)
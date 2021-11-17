from django.contrib import admin

# Register your models here.

from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone', 'email', 'criacao', 'atualizacao')
    #prepopulated_fields = {'slug': ('nome',)}

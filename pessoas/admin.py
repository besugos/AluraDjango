from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome_pessoa', 'email_pessoa')
    list_display_links = ('nome_pessoa', 'email_pessoa')
    search_fields = ('nome_pessoa',)
    list_per_page = 2

admin.site.register(Pessoa, ListandoPessoas)


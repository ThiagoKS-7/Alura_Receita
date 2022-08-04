from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ("id", "nome_pessoa", "idade", "email","telefone")
    list_display_links = ("id", "nome_pessoa")
    search_fields = ("nome_pessoa",)
    list_per_page = 10

admin.site.register(Pessoa,ListandoPessoas)


# Register your models here.

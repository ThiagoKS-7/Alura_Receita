from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ("id", "nome_receita", "categoria","pessoa","data_receita", "publicada")
    list_display_links = ("id", "nome_receita")
    search_fields = ("nome_receita",)
    list_filter = ("categoria",)
    list_editable  = ("publicada",)
    list_per_page = 10


# Register your models here.
admin.site.register(Receita, ListandoReceitas)

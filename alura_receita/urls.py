"""alura_receita URL Configuration
   É o router do django
"""
from django.contrib import admin
from django.urls import path, include

#url patterns = lista de rotas
urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
]

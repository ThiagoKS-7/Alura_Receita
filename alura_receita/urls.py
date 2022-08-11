"""alura_receita URL Configuration
   É o router do django
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#url patterns = lista de rotas
# o + static é pra usar a media do app receitas
urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

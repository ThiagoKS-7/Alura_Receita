from django.urls import path

from . import views # manipula qual url exibir

#lista de rotas
urlpatterns = [
    path('', views.index, name='index')
]
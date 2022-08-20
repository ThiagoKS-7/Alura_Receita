from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by("data_receita").filter(publicada=True)
    data = {
        "receitas": receitas,
    }
    return render(request, "index.html", data)


def receitas(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    data = {"receita": receita}
    return render(request, "receitas.html", data)


def buscar(request):
    lista_receitas = Receita.objects.order_by("data_receita").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if buscar:
            # procura todo nome que contenha o que for escrito no campo de busca
            lista_receitas = lista_receitas.filter(
                nome_receita__icontains=nome_a_buscar
            )
    data = {"receitas": lista_receitas}
    return render(request, "buscar.html", data)

from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.all()
    data = {
        'receitas': receitas,
    }
    return render(request,'index.html', data);
    
def receitas(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    data = {
        'receita': receita
    }
    return render(request,'receitas.html', data);
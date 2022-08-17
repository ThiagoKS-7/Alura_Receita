from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, "cadastro.html")


def login(request):
    return render(request, "login.html")


def dashboard(request):
    pass


def logout(request):
    pass

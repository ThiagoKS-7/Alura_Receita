from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  # modelo de usuarios
from django.contrib import auth, messages

from receitas.models import Receita


def pwdsAreDiferent(data):
    return data["password"] != data["password2"]


def userEmailExists(data):
    return User.objects.filter(email=data["email"]).exists()


def createUser(data):
    # o que vem da reuquest é os names dos inputs
    user = User.objects.create_user(
        username=data["nome"], email=data["email"], password=data["password"]
    )
    user.save()


def isEmpty(data):
    return (
        not data["nome"].strip()
        or not data["email"].strip()
        or not data["password"].strip()
    )


def cadastro(request):
    if request.method == "POST":
        data = request.POST
        # checar se o campo tá em branco => if not nome.strip(): ~ aviso;
        if isEmpty(data):
            messages.error(
                request, "Preencha todos os campos! Nada pode ficar em branco!"
            )
            return redirect("cadastro")
        elif pwdsAreDiferent(data):
            messages.error(
                request, "Senhas não conferem! Corrija os campos e tente novamente."
            )
            return redirect("cadastro")
        elif userEmailExists(data):
            messages.error(
                request,
                "Usuário já cadastrado! Faça login ao invés de cadastrar novamente.",
            )
            return redirect("login")
        else:
            createUser(data)
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")
    return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        # o que vem da reuquest é os names dos inputs
        data = request.POST
        user = auth.authenticate(
            request, username=data["email"], password=data["password"]
        )
        if not data["email"].strip() or not data["password"].strip():
            messages.error(
                request, "Preencha todos os campos! Nada pode ficar em branco!"
            )
            return redirect("login")
        if user is not None:
            messages.success(request, "Usuário logado com sucesso!")
            auth.login(request, user)
            return redirect("dashboard")
        else:
            print("Email ou senha inválidos! Tente de novo")
            return redirect("login")

    return render(request, "usuarios/login.html")


def dashboard(request):
    if request.user.is_authenticated:
        # Trazer todas as receitas feitas pelo usuário logado
        receitas_query = Receita.objects.order_by("data_receita").filter(
            pessoa=request.user.id
        )
        data = {
            "receitas": receitas_query,
        }
        return render(request, "usuarios/dashboard.html", data)
    else:
        return redirect("index")


def logout(request):
    auth.logout(request)
    return redirect("index")


def cria_receita(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
            pessoa=user,  # pessoa que criou a receita
            nome_receita=data["nome_receita"],
            ingredientes=data["ingredientes"],
            modo_preparo=data["modo_preparo"],
            rendimento=data["rendimento"],
            tempo_preparo=data["tempo_preparo"],
            categoria=data["categoria"],
            foto_receita=files["foto_receita"],
            banner_receita=files["banner_receita"],
        )
        receita.save()
        messages.success(request, f"Receita {data['nome_receita']} criada com sucesso!")
        return redirect("dashboard")
    else:
        return render(request, "usuarios/cria_receita.html")

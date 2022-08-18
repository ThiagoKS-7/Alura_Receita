from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # modelo de usuarios


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
    print(f"Usuário {data['nome']} cadastrado com sucesso!")


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
            print("Preencha todos os campos! Nada pode ficar em branco!")
            return redirect("cadastro")
        elif pwdsAreDiferent(data):
            print("Senhas não conferem! Corrija os campos e tente novamente.")
            return redirect("cadastro")
        elif userEmailExists(data):
            print("Usuário já cadastrado! Faça login ao invés de cadastrar novamente.")
            return redirect("login")
        else:
            createUser(data)
            return redirect("login")
    return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        # o que vem da reuquest é os names dos inputs
        nome = request.POST["nome"]
        print(f"{nome} logado com sucesso!")
        return redirect("index")
    return render(request, "usuarios/login.html")


def dashboard(request):
    pass


def logout(request):
    pass

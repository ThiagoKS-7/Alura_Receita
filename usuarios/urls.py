from django.urls import path


from . import views  # manipula qual url exibir

# lista de rotas
urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar_tarefa/", views.cadastrar_tarefa, name="cadastrar_tarefa"),
    path("listar_tarefa/", views.listar_tarefa, name="listar_tarefa"),
]

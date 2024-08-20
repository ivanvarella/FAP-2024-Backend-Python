from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar_tarefa/", views.cadastrar_tarefa, name="cadastrar_tarefa"),
    path("listar_tarefas/", views.listar_tarefas, name="listar_tarefas"),
    path("editar_tarefa/<int:tarefa_id>/", views.editar_tarefa, name="editar_tarefa"),
    path("excluir_tarefa/<int:tarefa_id>/", views.excluir_tarefa, name="excluir_tarefa"),
]

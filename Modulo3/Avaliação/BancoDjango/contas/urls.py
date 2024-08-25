from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar_conta/", views.cadastrar_conta, name="cadastrar_conta"),
    path("conta_cliente/", views.conta_cliente, name="conta_cliente"),
    path("listar_contas/", views.listar_contas, name="listar_contas"),
    # path("listar_contas/", views.listar_contas, name="listar_contas"),
    # path("editar_conta/<int:conta_id>/", views.editar_conta, name="editar_conta"),
    # path("excluir_conta/<int:conta_id>/", views.excluir_conta, name="excluir_conta"),
    # path("", views.listar_tarefas, name="home"),
]

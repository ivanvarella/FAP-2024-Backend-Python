# Django DRF
from rest_framework import viewsets

# Para adicionar as permissões
from rest_framework import permissions

# PAra permissões personalizadas
from tarefas.permissions import TarefaUserPermission

# Django RQL
from dj_rql.drf import RQLFilterBackend
from tarefas.filters import TarefaFilterClass

# Para conseguir acessar a tabela Tarefas do banco de dados
# Usando o ORM do Django com a classe em models do App Tarefas
from .models import Tarefas

# Serializers
from tarefas.serializers import TarefaModelSerializer


# Create your views here.


# ViewSet
class TarefaModelViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefaModelSerializer
    # Configs do RQL:
    filter_backends = [RQLFilterBackend]
    rql_filter_class = TarefaFilterClass
    # Permissões
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]  # Aqui perde todas as permissões e a API volta a ser acessada livremente

    # Usando permissões personalizadas:
    # A configuração abaixo: respeite o DjangoModelPermissions e também a permissão personalizada TarefaUserPermission
    # Respeitando-se a order, logo, a DjangoModelPermitions primeiro que a TarefaUserPermission
    permission_classes = [
        permissions.DjangoModelPermissions,
        TarefaUserPermission,
    ]

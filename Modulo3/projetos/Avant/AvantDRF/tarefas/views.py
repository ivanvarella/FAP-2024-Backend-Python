# Django DRF
from rest_framework import viewsets

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

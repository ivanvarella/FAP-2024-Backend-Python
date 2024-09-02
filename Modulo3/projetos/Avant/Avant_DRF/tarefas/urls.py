from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tarefas.views import TarefaModelViewSet


router = DefaultRouter()
router.register("tarefas", TarefaModelViewSet)  # Rota -> end point


# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]

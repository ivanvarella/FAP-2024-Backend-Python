from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("tarefas.urls")),
]


# Old: Sem API
# from django.contrib import admin
# from django.urls import path, include

# # Imports para o funcionamento das imagens (MEDIA)
# from django.conf import (
#     settings,
# )  # É o import do arquivo settings.py mesmo, para poder pegar o MEDIA_URL e o MEDIA_ROOT de lá
# from django.conf.urls.static import (
#     static,
# )  # Esse é aquele static lá que eu ainda não entendi muito - pesquisar mais...

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("usuarios/", include("usuarios.urls")),
#     path("tarefas/", include("tarefas.urls")),
#     path("", include("tarefas.urls")),  # Adicione essa linha
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

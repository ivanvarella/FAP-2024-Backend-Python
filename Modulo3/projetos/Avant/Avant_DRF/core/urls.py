from django.contrib import admin
from django.urls import path, include

# Para o simpleJWT -> Criando o alias de views para não confundir com a views do Django
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rotas para autenticação com o SimpleJWT
    path(
        "api/v1/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/v1/", include("tarefas.urls")),
]

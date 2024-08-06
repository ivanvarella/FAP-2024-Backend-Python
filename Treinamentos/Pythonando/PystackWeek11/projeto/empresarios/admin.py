from django.contrib import admin

# Register your models here.


# Adicionar a classe empresarios na área administrativa do Django
from .models import Empresas

admin.site.register(Empresas)

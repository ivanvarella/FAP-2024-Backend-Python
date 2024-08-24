from django.contrib import admin

# Register your models here.
from .models import Conta


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ("numero_conta", "nome", "tipo_conta", "saldo", "ativa")
    search_fields = ("nome", "numero_conta")
    ordering = (
        "-data_abertura",
    )  # Ordena por data de abertura, do mais recente para o mais antigo
    list_filter = ("tipo_conta", "ativa")
    fieldsets = (
        (None, {"fields": ("nome", "numero_conta")}),
        ("Saldo e Limite", {"fields": ("saldo", "limite_especial")}),
        ("Status", {"fields": ("ativa", "data_abertura")}),
        ("Tipo de Conta", {"fields": ("tipo_conta",)}),
    )
    add_fieldsets = (
        (None, {"fields": ("nome", "tipo_conta", "saldo", "limite_especial")}),
    )
    readonly_fields = ("data_abertura",)

    def get_field_display(self, obj, field):
        return getattr(obj, field)

    get_field_display.short_description = "Display Field"


# Personalizando o título do modelo no admin
admin.site.site_header = "Administração do Banco"
admin.site.site_title = "Administração do Banco"
admin.site.index_title = "Painel de Administração"

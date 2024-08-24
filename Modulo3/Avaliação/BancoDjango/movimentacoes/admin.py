from django.contrib import admin

# Register your models here.

from .models import Movimentacao


class MovimentacaoAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista
    list_display = ("data_movimentacao", "tipo_movimentacao", "valor", "conta")

    # Campos filtráveis na barra lateral
    list_filter = ("tipo_movimentacao", "data_movimentacao")

    # Campos pesquisáveis
    search_fields = ("conta__numero_conta", "tipo_movimentacao")

    # Exibição detalhada na visualização do objeto
    fields = ("data_movimentacao", "tipo_movimentacao", "valor", "conta")
    readonly_fields = ("data_movimentacao",)

    # Formatação personalizada do campo tipo_movimentacao na visualização da lista
    def get_tipo_movimentacao_display(self, obj):
        return obj.get_tipo_movimentacao_display()

    # Adiciona uma visualização personalizada do valor formatado como moeda
    def valor_formatado(self, obj):
        return f"R${obj.valor:,.2f}"

    valor_formatado.short_description = "Valor"

    # Adiciona a coluna valor_formatado à lista de exibição
    list_display = (
        "data_movimentacao",
        "get_tipo_movimentacao_display",
        "valor_formatado",
        "conta",
    )


# Registra o modelo e a configuração personalizada no admin
admin.site.register(Movimentacao, MovimentacaoAdmin)

from django.contrib import admin
from .models import Tarefas

# Register your models here.


@admin.register(Tarefas)
class TarefasAdmin(admin.ModelAdmin):
    list_display = (
        "descricao",
        "status",
        "prioridade",
        "progresso_conclusao",
        "dataInicio",
        "dataFim",
        "dataLimite",
        "user",
    )
    list_filter = ("status", "prioridade", "user")
    search_fields = ("descricao", "obs", "user__username")
    date_hierarchy = "dataInicio"
    ordering = ("status", "prioridade", "dataLimite")

    fieldsets = (
        (None, {"fields": ("descricao", "obs", "user")}),
        (
            "Status e Prioridade",
            {"fields": ("status", "prioridade", "progresso_conclusao")},
        ),
        ("Datas", {"fields": ("dataFim", "dataLimite")}),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by("dataInicio", "status")

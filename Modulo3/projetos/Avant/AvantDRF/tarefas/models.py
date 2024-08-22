from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tarefas(models.Model):
    status_choices = (
        (1, "Pendente"),
        (2, "Iniciado"),
        (3, "Concluído"),
        (4, "Excluído"),
    )
    prioridade_choices = (
        (1, "Baixa"),
        (2, "Média"),
        (3, "Alta"),
    )

    descricao = models.CharField(
        max_length=255, verbose_name="Descrição", null=False, blank=False
    )
    status = models.IntegerField(
        choices=status_choices, default=1, verbose_name="Status"
    )
    prioridade = models.IntegerField(
        choices=prioridade_choices, default=1, verbose_name="Prioridade"
    )
    obs = models.TextField(blank=True, null=True)
    progresso_conclusao = models.IntegerField(default=0, blank=True, null=True)
    dataInicio = models.DateTimeField(auto_now_add=True)
    dataFim = models.DateTimeField(blank=True, null=True)
    dataLimite = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

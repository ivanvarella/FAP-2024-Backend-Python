from django.db import models

# Create your models here.
from contas.models import (
    Conta,
)  # Certifique-se de que o App `Conta` esteja listado em INSTALLED_APPS


class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO_CHOICES = [
        ("deposito", "Depósito"),
        ("saque", "Saque"),
        ("transferencia", "Transferência"),
    ]

    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo_movimentacao = models.CharField(
        max_length=50, choices=TIPO_MOVIMENTACAO_CHOICES
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_movimentacao.capitalize()} de R${self.valor} em {self.data_movimentacao}"

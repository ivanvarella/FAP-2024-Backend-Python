from django.db import models

# Create your models here.
from contas.models import Conta


class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO_CHOICES = [
        (1, "Abertura de Conta"),
        (2, "Depósito"),
        (3, "Saque"),
        (4, "Transferência"),
        (5, "Encerramento de Conta"),
    ]

    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo_movimentacao = models.IntegerField(choices=TIPO_MOVIMENTACAO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    def __str__(self):
        tipo_movimentacao_display = self.get_tipo_movimentacao_display()
        return f"{tipo_movimentacao_display} de R${self.valor} em {self.data_movimentacao.strftime('%d/%m/%Y %H:%M')}"

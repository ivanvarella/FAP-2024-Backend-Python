from django.db import models
from contas.models import Conta
from decimal import Decimal


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
    saldo_antes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_apos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        tipo_movimentacao_display = self.get_tipo_movimentacao_display()
        return f"{tipo_movimentacao_display} de R${self.valor} em {self.data_movimentacao.strftime('%d/%m/%Y %H:%M:%S')}"

    def save(self, *args, **kwargs):
        if self.tipo_movimentacao == 1:  # Abertura de conta
            # Abertura de Conta: saldo_antes e saldo_apos será o valor da movimentação
            self.saldo_antes = self.valor
            self.saldo_apos = self.valor
        else:
            # Para outros tipos de movimentação, o saldo_antes deve ser calculado com base na última movimentação
            ultima_movimentacao = (
                Movimentacao.objects.filter(conta=self.conta)
                .order_by("-data_movimentacao")
                .first()
            )
            if ultima_movimentacao:
                self.saldo_antes = ultima_movimentacao.saldo_apos
            else:
                self.saldo_antes = Decimal("0.00")

            # Calcula o saldo_apos com base no tipo de movimentação
            if self.tipo_movimentacao == 2:  # Deposito
                # Depósito: adiciona o valor ao saldo_antes
                self.saldo_apos = self.saldo_antes + self.valor
            elif self.tipo_movimentacao == 3:  # Saque
                # Saque: subtrai o valor do saldo_antes
                self.saldo_apos = self.saldo_antes - self.valor
            elif self.tipo_movimentacao == 4:  # Transferencia
                # Transferência: subtrai o valor do saldo_antes
                self.saldo_apos = self.saldo_antes - self.valor
            elif self.tipo_movimentacao == 5:  # Encerramento de conta
                # Encerramento de Conta: saldo_apos deve ser 0
                self.saldo_apos = 0

        super().save(*args, **kwargs)

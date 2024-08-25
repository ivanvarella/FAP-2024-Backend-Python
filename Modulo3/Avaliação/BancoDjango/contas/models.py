from django.db import models
import random
from django.contrib.auth.models import User


class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        (1, "Conta Corrente"),
        (2, "Conta Poupança"),
    ]
    numero_conta = models.IntegerField(unique=True)
    data_abertura = models.DateTimeField(auto_now_add=True)
    tipo_conta = models.IntegerField(choices=TIPO_CONTA_CHOICES)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    limite_especial = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    ativa = models.BooleanField(default=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Id do usuário: {self.id_user} - Número da conta: {self.numero_conta} - Saldo: {self.saldo}"

    @staticmethod
    def gerar_numero_conta_unico():
        # Gera um número aleatório de 6 dígitos
        numero = random.randint(100000, 999999)
        # Verifica se já existe uma conta com esse número
        while Conta.objects.filter(numero_conta=numero).exists():
            numero = random.randint(100000, 999999)
        return numero

    def _criar_movimentacao(self, tipo, valor):
        # Importação atrasada para evitar importações circulares
        from movimentacoes.models import Movimentacao

        # Cria uma movimentação associada à conta
        Movimentacao.objects.create(
            tipo_movimentacao=tipo,
            conta=self,
            valor=valor,
        )

    def save(self, *args, **kwargs):
        # Verifica se a instância é nova (não tem ID ainda)
        is_new = not self.pk

        if is_new:
            # Gera um número de conta único para novas contas
            self.numero_conta = self.gerar_numero_conta_unico()

        # Salva a conta no banco de dados
        super().save(*args, **kwargs)

        # Cria uma movimentação de "Abertura de Conta" para novas contas
        if is_new:
            self._criar_movimentacao(tipo=1, valor=self.saldo)
        # Cria uma movimentação de "Encerramento de Conta" se a conta for encerrada
        elif not self.ativa:
            self._criar_movimentacao(tipo=5, valor=0)

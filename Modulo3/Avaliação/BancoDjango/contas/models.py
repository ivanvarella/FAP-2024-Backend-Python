from django.db import models
import random


class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        (1, "Conta Corrente"),
        (2, "Conta Poupança"),
    ]

    numero_conta = models.IntegerField(unique=True)
    data_abertura = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255)
    tipo_conta = models.IntegerField(choices=TIPO_CONTA_CHOICES)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    limite_especial = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"Nome: {self.nome} - Número da conta: {self.numero_conta} - Saldo: {self.saldo}"

    @staticmethod
    def gerar_numero_conta_unico():
        # Gera um número aleatório de 6 dígitos
        numero = random.randint(100000, 999999)
        # Verifica se já existe uma conta com esse número
        while Conta.objects.filter(numero_conta=numero).exists():
            numero = random.randint(100000, 999999)
        return numero

    # Alterando o comportamente do método save() do Django
    def save(self, *args, **kwargs):
        # Verifica se a instância é nova (não tem ID ainda)
        is_new = not self.pk

        # Se for uma conta nova, gera o numero_conta e salva na tabela do App conta
        if is_new:
            self.numero_conta = self.gerar_numero_conta_unico()

            super().save(*args, **kwargs)  # Salva a conta no banco de dados

            # Cria a movimentação correspondente
            # Se for conta nova, cria movimantacao de abertura de conta
            # Importação atrasada, corrige o problema de importações circulares, onde dois módulos importam um ao outro
            from movimentacoes.models import Movimentacao

            Movimentacao.objects.create(
                tipo_movimentacao=1,  # "Abertura de Conta"
                conta=self,  # Passa os dados de conta para pegar o pk daqui como fk lá
                valor=self.saldo,
            )

        # Se a conta já existir e estiver sendo encerrada, cria movimentacao de encerramento de conta
        elif not self.ativa:

            # Importação atrasada
            from movimentacoes.models import Movimentacao

            Movimentacao.objects.create(
                tipo_movimentacao=5,  # "Encerramento de Conta"
                conta=self,
                # Fazer uma verificação na views para caso exista saldo na conta, não permitir encerrar a conta
                # Se chegou aqui é pq essa verificação já foi feita, então encerre a conta
                valor=0,
            )

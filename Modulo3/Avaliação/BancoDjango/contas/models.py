from django.db import models


# Create your models here.
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
        return f"{self.nome} - {self.numero_conta}"

from conta import Conta


conta1 = Conta("Ivan Varella", 1000, 500, 2).criar_conta()


# def __init__(self, nome, saldo=0, limite_especial=0, tipo_conta=1):
#         """Inicializa uma conta com saldo e limite especial."""
#         self.nome = nome
#         self.data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M")
#         self.saldo = saldo
#         self.limite_especial = limite_especial
#         self.tipo_conta = tipo_conta
#         self.operações = [(self.data_abertura, "ABERTURA DE CONTA", saldo)]

from datetime import datetime

global contas
contas = []


class Conta:
    def __init__(self, nome, saldo=0, limite_especial=0):
        """Inicializa uma conta com saldo e limite especial."""
        self.numero_conta = self.gerar_numero_conta()
        self.nome = nome
        self.data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.saldo = saldo
        self.limite_especial = limite_especial
        self.operações = [(self.data_abertura, "ABERTURA DE CONTA", saldo)]

        # Adiciona a conta à lista de contas
        contas.append(self)

    @staticmethod
    def gerar_numero_conta():
        """Gera um número de conta único."""
        if not contas:
            return 1  # Se não houver contas, o primeiro número é 1

        numeros_existentes = {conta.numero_conta for conta in contas}
        numero = 1

        while numero in numeros_existentes:
            numero += 1

        return numero

    def depositar(self, valor):
        """Deposita um valor na conta, deve ser positivo."""
        if valor > 0:
            self.saldo += valor
            self.operações.append(
                (datetime.now().strftime("%Y-%m-%d %H:%M"), "DEPÓSITO", valor)
            )
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta, utilizando o limite especial se necessário."""
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return

        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(
                (datetime.now().strftime("%Y-%m-%d %H:%M"), "SAQUE", -valor)
            )
        elif self.saldo + self.limite_especial >= valor:
            self.saldo -= valor
            self.operações.append(
                (datetime.now().strftime("%Y-%m-%d %H:%M"), "SAQUE LIMITE", -valor)
            )
            print(
                f"Saldo insuficiente. Usando limite especial. Novo saldo: R${self.saldo:.2f}"
            )
        else:
            print(
                f"Saldo insuficiente. Seu saldo atual é de R${self.saldo:.2f} e seu limite especial é de R${self.limite_especial:.2f}."
            )

    def exibir_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        """Exibe o extrato das operações realizadas na conta."""
        print(f"Extrato CC N° {self.numero_conta}\n")
        for operacao in self.operações:
            data, descricao, valor = operacao
            print(f"{data} {descricao:<20} R${valor:10.2f}")
        print(f"\nSaldo atual: R${self.saldo:.2f}\n")


# Teste:
# conta1 = Conta(nome="João", saldo=100, limite_especial=200)
# conta2 = Conta(nome="Ricardo", saldo=1000, limite_especial=500)
# conta3 = Conta(nome="Luiz", saldo=800, limite_especial=300)
# conta1 = Conta(nome="Ivan", saldo=300, limite_especial=50)
# for conta in contas:
#     print(conta.nome)
#     print(conta.numero_conta)
#     print(conta.data_abertura)
#     print(conta.saldo)
#     print(conta.limite_especial)
#     print("\n")


# conta1.sacar(150)
# conta1.exibir_saldo()

# # Excluir a conta para testar a geração de número único
# contas.remove(conta1)

# conta2 = Conta(
#     nome="Maria", data_abertura=datetime.now(), saldo=50, limite_especial=100
# )
# print(f"Número da nova conta: {conta2.numero_conta}")

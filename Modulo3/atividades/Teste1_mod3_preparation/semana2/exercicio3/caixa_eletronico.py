class Conta:
    def __init__(self, saldo=0, limite_especial=0):
        """Inicializa uma conta com saldo e limite especial."""
        self.saldo = saldo
        self.limite_especial = limite_especial

    def depositar(self, valor):
        """Deposita um valor na conta, deve ser positivo."""
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta, utilizando o limite especial se necessário."""
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return

        if self.saldo >= valor:
            self.saldo -= valor
        elif self.saldo + self.limite_especial >= valor:
            self.saldo -= valor
        else:
            print(
                f"Saldo insuficiente. Seu saldo atual é de R${self.saldo:.2f} e seu limite especial é de R${self.limite_especial:.2f}"
            )

    def exibir_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual: R${self.saldo:.2f}")


# Exemplo de uso:
conta = Conta(saldo=100, limite_especial=50)
conta.exibir_saldo()  # Exibe: Saldo atual: R$100.00
conta.depositar(50)
conta.exibir_saldo()  # Exibe: Saldo atual: R$150.00
conta.sacar(200)
conta.exibir_saldo()  # Exibe: Saldo atual: R$-50.00
conta.sacar(
    10
)  # Exibe: Saldo insuficiente. Seu saldo atual é de R$-50.00 e seu limite especial é de R$50.00

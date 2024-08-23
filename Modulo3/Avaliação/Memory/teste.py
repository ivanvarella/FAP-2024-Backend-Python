from conta import Conta


def testar_conta():
    print("### TESTE MANUAL DA CLASSE CONTA ###\n")

    # Criando uma conta para o teste
    conta = Conta(nome="Teste", saldo=100, limite_especial=200)
    print(
        f"Conta criada com número: {conta.numero_conta}, Nome: {conta.nome}, Saldo: R${conta.saldo}, Limite especial: R${conta.limite_especial}\n"
    )

    # Testando depósito
    print("Testando depósito de R$50.00...")
    conta.depositar(50)
    conta.exibir_saldo()
    print()

    # Testando depósito com valor negativo
    print("Testando depósito de valor negativo R$-50.00...")
    conta.depositar(-50)
    conta.exibir_saldo()
    print()

    # Testando saque com saldo suficiente
    print("Testando saque de R$30.00 com saldo suficiente...")
    conta.sacar(30)
    conta.exibir_saldo()
    print()

    # Testando saque usando o limite especial
    print("Testando saque de R$250.00 usando limite especial...")
    conta.sacar(250)
    conta.exibir_saldo()
    print()

    # Testando saque acima do saldo e limite especial
    print("Testando saque de R$350.00 acima do saldo e limite especial...")
    conta.sacar(350)
    conta.exibir_saldo()
    print()

    # Exibindo o extrato
    print("Exibindo o extrato da conta...")
    conta.extrato()
    print("### FIM ####")


testar_conta()

# contas é variável global do arquivo conta.py, porém está limitada ao escopo do próprio arquivo
from conta import Conta, contas
import os


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def criar_conta():
    nome = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    limite_especial = float(input("Digite o limite especial: "))
    conta = Conta(nome, saldo_inicial, limite_especial)
    print(f"Conta criada com sucesso! Número da conta: {conta.numero_conta}\n")


def realizar_deposito():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor a ser depositado: "))
    conta = encontrar_conta(numero)
    if conta:
        conta.depositar(valor)
        print("Depósito realizado com sucesso!\n")
    else:
        print("Conta não encontrada.\n")


def realizar_saque():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor a ser sacado: "))
    conta = encontrar_conta(numero)
    if conta:
        conta.sacar(valor)
    else:
        print("Conta não encontrada.\n")


def exibir_saldo():
    numero = int(input("Digite o número da conta: "))
    conta = encontrar_conta(numero)
    if conta:
        conta.exibir_saldo()
    else:
        print("Conta não encontrada.\n")


def exibir_extrato():
    numero = int(input("Digite o número da conta: "))
    conta = encontrar_conta(numero)
    if conta:
        conta.extrato()
    else:
        print("Conta não encontrada.\n")


def encontrar_conta(numero):
    for conta in contas:
        if conta.numero_conta == numero:
            return conta
    return None


def listar_contas():
    """Lista todas as contas cadastradas."""
    if not contas:
        print("\nNão há contas cadastradas.\n\n")
    else:
        print("Listagem de Contas:")
        for conta in contas:
            print(f"Número da conta: {conta.numero_conta}")
            print(f"Nome do titular: {conta.nome}")
            print(f"Saldo atual: R${conta.saldo:.2f}")
            print("-" * 30)


def menu_principal():
    opcoes = ["1", "2", "3", "4", "5", "6", "7"]
    while True:
        print("1. Criar conta")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Exibir saldo")
        print("5. Exibir extrato")
        print("6. Listar contas cadastradas")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao not in opcoes:
            input("Opção inválida. Enter para voltar.")
            continue
        else:
            if opcao == "1":
                limpar_tela()
                criar_conta()
                menu_principal()
            elif opcao == "2":
                limpar_tela()
                realizar_deposito()
                menu_principal()
            elif opcao == "3":
                limpar_tela()
                realizar_saque()
                menu_principal()
            elif opcao == "4":
                limpar_tela()
                exibir_saldo()
                menu_principal()
            elif opcao == "5":
                limpar_tela()
                exibir_extrato()
                menu_principal()
            elif opcao == "6":
                limpar_tela()
                listar_contas()
                menu_principal()
            elif opcao == "7":
                limpar_tela()
                print("\n\nPrograma encerrado.\n\n")
                break


menu_principal()

while True:
    num1 = input(
        "Digite o número para verificação (Par ou Ímpar) ou 'sair' para encerrar: "
    )

    if num1.lower() == "sair":
        break

    # Verifica se a entrada é um número válido
    try:
        num1 = int(num1)
    except ValueError:
        print("Digite um número válido")
        continue

    num1 = int(num1)

    (
        print(f"O número {num1} é Par")
        if num1 % 2 == 0
        else print(f"O número {num1} é ímpar")
    )

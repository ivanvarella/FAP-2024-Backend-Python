def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."


# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza as operações e exibe os resultados
print(f"Soma: {somar(numero1, numero2)}")
print(f"Subtração: {subtrair(numero1, numero2)}")
print(f"Multiplicação: {multiplicar(numero1, numero2)}")
print(f"Divisão: {dividir(numero1, numero2)}")

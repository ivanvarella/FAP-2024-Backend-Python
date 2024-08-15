class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Erro: Divisão por zero não é permitida."


while True:

    # Solicita os números ao usuário
    numero1 = input("Digite o primeiro número ou sair: ")
    if numero1 == "sair":
        break
    numero2 = input("Digite o segundo número ou sair: ")
    if numero2 == "sair":
        break
    # Solicita ao usuário que escolha uma operação
    operacao = input(
        "Escolha a operação (1: soma, 2: subtracao, 3: multiplicacao, 4: divisao) ou sair: "
    )
    if operacao == "sair":
        break

    numero1 = float(numero1)
    numero2 = float(numero2)
    operacao = int(operacao)

    # Instancia a calculadora
    calculadora = Calculadora(numero1, numero2)

    operacoes_permitidas = [1, 2, 3, 4]

    if operacao not in operacoes_permitidas:
        print("Operação inválida")
    else:
        # Utiliza match-case para escolher a operação
        match operacao:
            case 1:
                print(f"Soma: {calculadora.somar()}")
            case 2:
                print(f"Subtração: {calculadora.subtrair()}")
            case 3:
                print(f"Multiplicação: {calculadora.multiplicar()}")
            case 4:
                print(f"Divisão: {calculadora.dividir()}")
            case _:
                print("Operação inválida")

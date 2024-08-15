# Funções lambda para cada operação
funcoes_operacoes = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: (
        a / b if b != 0 else "Erro: Divisão por zero não é permitida."
    ),
}

# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Mapeamento das opções do usuário para as operações
operacoes = {"1": "soma", "2": "subtracao", "3": "multiplicacao", "4": "divisao"}

# Solicita ao usuário que escolha uma operação
operacao = input(
    "Escolha a operação (1: soma, 2: subtracao, 3: multiplicacao, 4: divisao): "
)

# Obtém o nome da operação escolhida
operacao_escolhida = operacoes.get(operacao)

# Verifica se a operação escolhida é válida e executa a função correspondente
if operacao_escolhida in funcoes_operacoes:
    resultado = funcoes_operacoes[operacao_escolhida](numero1, numero2)
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida")

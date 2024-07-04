# Decomposição de Cédulas: Escreva um programa que leia um valor em reais
# (R$) e calcule a quantidade mínima de cédulas necessárias para representar esse
# valor. Considere cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e R$ 1.

import funcoesSuporte


valor, erroTipoValor, erroVazioValor, erroMsgValor = funcoesSuporte.isValidInput("\n\nDigite o valor para decomposição de cédulas: ", "int")

print("-"*50)

cedulas=0
atual=100
apagar=valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:  # Verifica se alguma cédula foi contada
            print(f"{cedulas} cédula(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
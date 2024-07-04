# 5. Gerador de Intervalo: Faça um programa que receba dois números inteiros e gere
# os números inteiros que estão no intervalo entre eles, inclusive.

import funcoesSuporte as func
import time

def gerarIntervaloNumeros(numero1, numero2):
  return range(numero1+1, numero2)

def exibirIntervalo(intervalo):
    for i, numero in enumerate(intervalo):
        if i < len(intervalo) - 1:
            print(numero, end=", ")
        else:
            print(numero)

numero1, erroTipoNumero1, erroVazioNumero1, erroMsgNumero1 = func.isValidInput("\n\nDigite o primeiro número inteiro: ", "int")

numero2, erroTipoNumero2, erroVazioNumero2, erroMsgNumero2 = func.isValidInput("\nDigite o segundo número inteiro: ", "int")

print(f"\n\nGerando intervalo de números inteiros entre {numero1} e o número {numero2}.")

intervalo = gerarIntervaloNumeros(numero1, numero2)
time.sleep(2)

print("\nIntervalo gerado: ")
exibirIntervalo(intervalo)
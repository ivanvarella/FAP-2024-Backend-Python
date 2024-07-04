# 7. Contador de Intervalos: Faça um programa que leia uma quantidade
# indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar
# quando for lido um número negativo.

import funcoesSuporte as func


def contarIntervalos(numero, qtdIntervalos):
  if numero >= 0 and numero <= 25:
    qtdIntervalos[0] += 1
  elif numero >= 26 and numero <= 50:
    qtdIntervalos[1] += 1
  elif numero >= 51 and numero <= 75:
    qtdIntervalos[2] += 1
  elif numero >= 76 and numero <= 100:
    qtdIntervalos[3] += 1
  else:
    print("Número fora do intervalo válido, não será registrado.")
  return qtdIntervalos

# Inicializa a lista com com a qtd de números em cada intervalo, é atualizado pela função contarIntervalos
qtdIntervalos = [0, 0, 0, 0]  # [0-25], [26-50], [51-75] e [76-100]
while True:
  numero, erroTipoNumero, erroVazioNumero, erroMsgNumero = func.isValidInput("\n\nDigite um número positivo (-1 para sair): ", "float")

  if numero < 0:
    break

  qtdIntervalos = contarIntervalos(numero, qtdIntervalos)

# Exibe os resultados
faixas = ["0-25", "26-50", "51-75", "76-100"]
print("\n\nResultados:")
print(f"Quantidade Intervalo: {qtdIntervalos}")
for i in range(len(faixas)):
    print(f"Faixa {faixas[i]}: {qtdIntervalos[i]} números")

# 4. Caloculadora de Desconto de Combustível: Implemente um programa para um
# posto de gasolina que calcule o valor a ser pago pelo cliente, considerando o tipo
# de combustível (álcool ou gasolina) e a quantidade de litros. Use a seguinte
# tabela de desconts:
# 
# * Álcool: até 20 litros (3% por litro), acima de 20 litros (5% por litro)
# * Gasolina: até 20 litros (4% por litro), acima de 20 litros (6% por litro) Preços
# base: Álcool R$ 1,90/litro, Gasolina R$ 2,50/litro

import funcoesSuporte


def calculaDesconto(tipo, litros):
    if tipo == 1:
        if litros <= 20:
            desconto = litros * 0.03
            valorTotal = 1.90 * litros - desconto
        else:
            desconto = litros * 0.05
            valorTotal = 1.90 * litros - desconto
    elif tipo == 2:
        if litros <= 20:
            desconto = litros * 0.04
            valorTotal = 2.50 * litros - desconto
        else:
            desconto = litros * 0.06
            valorTotal = 2.50 * litros - desconto
    return desconto, valorTotal

# Verifica opção escolhida
while True:
  opcaoCombustivel, erroTipoOpcaoCombustivel, erroVazioOpcaoCombustivel, erroMsgOpcaoCombustivel = funcoesSuporte.isValidInput("\nEscolha o tipo de combustível 1 - álcool / 2 = gasolina: ", "int")
  if opcaoCombustivel not in (1, 2):
    print("\nOpção inválida\n")
  else:
    break

# Verifica quantidade de litros
while True:
  litros, erroTipoLitros, erroVazioLitros, erroMsgLitros = funcoesSuporte.isValidInput("\nQuantos litros: ", "float")
  if litros <= 0:
    print("\nA quantidade de litros deve ser maior que 0.\n")
  else:
    break

desconto, valorTotal = calculaDesconto(opcaoCombustivel, litros)

print(f"\nO desconto recebido foi de R$ {desconto:.2f} reais e o valor a ser pago é R$ {valorTotal:.2f}.")
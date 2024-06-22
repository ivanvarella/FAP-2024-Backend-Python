##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####

print("\n++++  Cálculo IRPF  ++++\n\n")

import os
import json

nomeArquivo = 'aliquotas.json'
caminhoRelativo = os.getcwd() + "/Modulo1/atividades/10-06-2024/irpf/" + nomeArquivo
file = caminhoRelativo


def readJson(file):
  with open(file, 'r') as f:
    data = json.load(f)
  return data

def calcImposto(salario, aliquota, deducao):
  return (salario * aliquota) - deducao

#Carrega dados Json
DataAliquotas = readJson(file)
aliquotas = DataAliquotas['aliquotas']

def determinarFaixa(salario, aliquotas):
  if salario > 4664.68:
    faixa = aliquotas[4]
  elif (salario >= 3751.06) and (salario <= 4664.68):
    faixa = aliquotas[3]
  elif (salario >= 2826.66) and (salario <= 3751.05):
    faixa = aliquotas[2]
  elif (salario >= 2259.21) and (salario <= 2826.65):
    faixa = aliquotas[1]
  elif (salario <= 2259.20):
    faixa = aliquotas[0]
  return faixa

salario = float(input("Digite o salário: "))

#Determina a faixa
faixa = determinarFaixa(salario, aliquotas)
#Calcula o imposto
imposto = round(calcImposto(salario, faixa['aliquota'], faixa['deducao']),2)

print(f"\n\nSalário: R$ {salario:.2f}")
print(f"\nFaixa: {faixa['faixa']} - Alíquota: {round(faixa['aliquota']*100,2)}%")
print(f"\nImposto pago: R${imposto} (Cálculo: R${salario} * {faixa['aliquota']} - R${faixa['deducao']})")
print(f"\nValor à receber após IR: R${salario - imposto}\n")

print("\n++++  FIM DO PROGRAMA  ++++\n")
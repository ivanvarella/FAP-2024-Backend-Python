import json
import os
import math

# Caminho do diretório atual
caminho = os.getcwd() + "/Modulo1/atividades/14-06-2024/deposito/"


# Função para adicionar nova bola ao Json
def cadastrarBola(novoNome, novoDiametro):
  file = caminho + 'bolas.json'
  with open(file, 'r') as f:
    data = json.load(f)

  # Se o Json estiver vazio -> inicializa o Objeto 'Bolas'
  if 'Bolas' not in data:
    data['Bolas'] = []

  # Add a bola ao Objeto
  data['Bolas'].append({'nome': novoNome, 'diametro': novoDiametro})

  # Adiciona a bola ao Json
  with open(file, 'w') as f:
    json.dump(data, f, indent=2)

# Carrega os dados do Json
def carregaDadosJson(file):
  file = caminho + file
  print(f"File dentro carregaJson: {file}")
  with open(file, 'r') as f:
    data = json.load(f)
  return data

# Calcula o volume do depósito
def calcVolumeDeposito(depositoAltura, depositoLargura, depositoProfundidade):
  return depositoAltura * depositoLargura * depositoProfundidade

# Dado o raio, calcula o volume de uma bola
def calcVolumeBola(raio):
  return (4/3) * math.pi * (raio ** 3)

# Conversão m3 -> cm3
def m3Tocm3(volumeM3):
    return volumeM3 * 1000000

# Conversão cm3 -> m3
def cm3Tom3(volumeCm3):
    return volumeCm3 / 1000000

# Calcula o máximo de bolas que cabem no depósito - aproximadamente: diametro = altura e largura do cubo
def calcMaxBolas(diametro, depositoVolume):
  volumeBolaCubo = diametro ** 3
  depositoVolumeCm3 = m3Tocm3(depositoVolume)
  maxBolas = depositoVolumeCm3 // volumeBolaCubo
  return maxBolas

# Função para validação de entradas input
# - msg: mensagem mostrada no input
# - tipoEsperado: "string", "int", "float", "intFloat" - "intFloat" podendo receber int ou float
# - aceitaVazio: padrão False (não aceitando valores vazios), caso aceite, declarar na chamada da função como True
# - Retorno da função: valor, erroTipo, erroVazio, msgErro
def isValidInput(msg, tipoEsperado, aceitaVazio = False):
  # Inicialização dos erros:
  erroTipo = False
  erroVazio = False
  erroMsg = ""
  valor = input(msg)

  while True:
    # Verifica se está vazio e se deveria estar
    if (aceitaVazio == False) and (len(valor) == 0):
      erroMsg = "Entrada vazia não é permitida."
      print(erroMsg)
      valor = input(msg)
    else:
      # Se o tipo esperado for string, todos os valores são aceitos
      if (tipoEsperado == "string"):
        erroTipo = False
        break
      elif (tipoEsperado == "int"):
        try:
            valor = int(valor)
            erroTipo = False
            break
        except ValueError:
            erroTipo = True
            erroMsg = "Entrada inválida. O valor deve ser um inteiro."
            print(erroMsg)
            valor = input(msg)
      elif (tipoEsperado == "float"):
        try:
            valor = float(valor)
            erroTipo = False
            break
        except ValueError:
            erroTipo = True
            erroMsg = "Entrada inválida. O valor deve ser um float."
            print(erroMsg)
            valor = input(msg)
      elif (tipoEsperado == "intFloat"):
        try:
            valor = float(valor)
            erroTipo = False
            break
        except ValueError:
            erroTipo = True
            erroMsg = "Entrada inválida. O valor deve ser um número."
            print(erroMsg)
            valor = input(msg)

  return valor, erroTipo, erroVazio, erroMsg
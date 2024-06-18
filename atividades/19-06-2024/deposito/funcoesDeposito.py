import json
import os
import math

# Caminho do diretório atual
caminho = os.getcwd() + "/atividades/19-06-2024/deposito/"

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
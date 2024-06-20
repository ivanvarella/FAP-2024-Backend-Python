import json
import os
from datetime import datetime

# Caminho do diretório atual
caminho = os.getcwd() + "/FAP-2024-Backend-Python/Modulo1/atividades/19-06-2024/guessGame/"

def calculaTempo(difTempo):
  segundosTotal = difTempo.total_seconds()
  if segundosTotal < 60:
    segundos = round(segundosTotal, 2)
    minutos = 0
    return minutos, segundos
  else:
    minutos = segundosTotal // 60
    segundos = segundosTotal % 60
    return minutos, segundos
import funcoesSuporte
from random import randint
import time
from datetime import datetime

def iniciarJogo():
  print("\n-----------------------------------------------")
  print("Computador gerando um número aleatório.")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  n1 = randint(1, 10)
  print("Número gerado com sucesso!\n")
  inicioContagemTempo = datetime.now()
  guess = int(input("Adivinhe qual foi o número:"))
  tentativas = 1

  if guess == n1:
    fimContagemTempo = datetime.now()
    horas, minutos, segundos = funcoesSuporte.calculaTempoDecorrido(fimContagemTempo - inicioContagemTempo)
    print("Parabéns, você acertou!")
    print(f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {horas} horas, {minutos} minutos e {segundos} segundos!\n\n")
  else:
    while guess != n1:
      if guess < n1:
        print("Errou, o número é maior!")
      else:
        print("Errou, o número é menor!")
      tentativas += 1
      guess = int(input("Tente novamente:"))
    fimContagemTempo = datetime.now()
    horas, minutos, segundos = funcoesSuporte.calculaTempoDecorrido(fimContagemTempo - inicioContagemTempo)
    print(f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {horas} horas, {minutos} minutos e {segundos} segundos!\n\n")
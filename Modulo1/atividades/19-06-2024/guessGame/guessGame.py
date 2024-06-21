##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####

import funcoesSuporte
from random import randint
import time
from datetime import datetime

print("Jogo Guess the number\n")

print("###### Selecione uma opção ######")
print("# Cod[1]: Mostrar recordes      #")
print("# Cod[2]: Iniciar jogo          #")
print("# Cod[3]: Sair                  #")
print("#################################\n")

codUser = (input("Digite o código:"))

while True:
    if codUser == "3":
        print("\nObrigado por jogar!\n\n")
    elif codUser == "1":
        # Falta fazer essa parte
        # funcoesSuporte.mostraRecordes()
        print("Em breve estará disponível!")
    elif codUser == "2":
        break
    else:
        print("\nOpção inválida!\n\n")

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
    minutos, segundos = funcoesSuporte.calculaTempo(fimContagemTempo - inicioContagemTempo)
    print("Parabéns, você acertou!")
    print(f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {minutos} minutos e {segundos} segundos! ")
else:
    while guess != n1:
        if guess < n1:
            print("Errou, o número é maior!")
        else:
            print("Errou, o número é menor!")
        tentativas += 1
        guess = int(input("Tente novamente:"))
    fimContagemTempo = datetime.now()
    minutos, segundos = funcoesSuporte.calculaTempo(fimContagemTempo - inicioContagemTempo)
    print(f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {minutos} minutos e {segundos} segundos! ")

'''
Falta:
1 - Função para gravar recordes Json - atenção para o formata da data e de tempo (caso decida inserir também)
2- "Formulário" com os dados do usuário para gravar no Json
2 - Função para ler recordes Json e exibir
3 - Melhorar a lógica do jogo quando está aproximando do valor a ser encontrado
'''
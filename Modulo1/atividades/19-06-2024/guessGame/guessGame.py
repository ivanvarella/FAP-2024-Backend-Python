##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####
##### Pedro Vinícius ####

from random import randint
import time

print("Jogo Guess the number\n\n")

print("Computador gerando um número.")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
n1 = randint(1, 10)
print("Número gerado com sucesso!\n")
guess = int(input("Adivinhe qual foi o número:"))
tentativas = 1

if guess == n1:
    print("Parabéns, você acertou!")
else:
    while guess != n1:
        if guess < n1:
            print("Errou, o número é maior!")
        else:
            print("Errou, o número é menor!")
        tentativas += 1
        guess = int(input("Tente novamente:"))
    print(f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas!")


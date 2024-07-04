# 1. Classificador de Nadadores: Crie um programa que leia a idade de um nadador e
# o classifique em uma das seguintes categorias:
# * Infantil A: 5 a 7 anos
# * Infantil B: 8 a 11 anos
# * Juvenil A: 12 a 13 anos
# * Juvenil B: 14 a 17 anos
# * Adultos: Maiores de 18 anos


import funcoesSuporte
import time

def classificarNadador(idade):
    if idade < 5:
        return "Sem classificação"
    elif idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 11:
        return "Infantil B"
    elif idade >= 12 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adultos"
    else:
        return "Idade inválida"
    
idade, erroTipoIdade, erroVazioIdade, erroMsgIdade = funcoesSuporte.isValidInput("\n\nDigite a idade do nadador: ", "int")

print("\nGerando classificação do nadador...")
time.sleep(0.8)

print("\nAcessando super computador na NASA...")
time.sleep(0.8)

print("\nConexão estabedlecida com sucesso!")
time.sleep(0.8)

print("\nCalculando... CPU em 100%... Overload CPU... Refrigeração com nitrogênio iniciada....")
time.sleep(0.8)

classificacao = classificarNadador(idade)

print("\nClassificação finalizada!")
time.sleep(0.8)

print(f"\nA classificação do nadador é: {classificacao}\n")
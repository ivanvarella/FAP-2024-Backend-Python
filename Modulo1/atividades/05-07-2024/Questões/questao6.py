# 6. Classificador de Turma por Idade: Crie um programa que peça a idade de várias
# pessoas. O programa deve parar quando o usuário digitar 0. Ao final, o
# programa deve calcular a média de idade e classificar a turma como:
# * Jovem: 0-25 anos
# * Adulta: 26-60 anos
# * Idosa: > 60 anos

import funcoesSuporte

def calculaMediaIdades(idades):
    return (sum(idades) / len(idades))

def classificaIdade(idades):
    
    mediaIdade = calculaMediaIdades(idades)

    if mediaIdade >= 0 and mediaIdade <= 25:
        return "Jovem", mediaIdade
    elif mediaIdade > 25 and mediaIdade <= 60:
        return "Adulta", mediaIdade
    else:
        return "Idosa", mediaIdade

# Obtém todas as idades:
idades = []
while True:
    idade, erroTipoIdade, erroVazioIdade, erroMsgIdade = funcoesSuporte.isValidInput("\nDigite a idade: ", "int")
    if idade == 0:
        break
    else:
        # Guarda a idade
        idades.append(idade)

# Classifica
classificacaoTurma, mediaIdade = classificaIdade(idades)

print(f"As idades da turma: {idades}.")

# Imprime
print(f"\nA média da idade da turma é de {mediaIdade:.2f}, logo a turma é classificada como {classificacaoTurma}.")
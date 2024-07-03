# 8. Sistema de Votação: Crie um programa que simule uma votação com 4
# candidatos. O programa deve contar os votos de cada candidato, votos nulos e
# em branco. Ao final, deve mostrar o total de votos para cada candidato, o total
# de votos nulos e em branco, e as respectivas porcentagens sobre o total de votos.


import funcoesSuporte

def exibeopcaoVotos():
  print("-"*27)
  print("- Escolha uma opção       -")
  print("-"*27)
  print("- [1] - Candidato 1       -")
  print("- [2] - Candidato 2       -")
  print("- [3] - Candidato 3       -")
  print("- [4] - Candidato 4       -")
  print("- [5] - Voto Nulo         -")
  print("- [6] - Voto em Branco    -")
  print("- [0] - Sair              -")
  print("-"*27)

def registraVotos(voto, votos):
  # Nulo
  if voto == 5:
    votos[4] += 1
  # Branco
  elif voto == 6:
    votos[5] += 1
  # Candidatos
  else:
    votos[voto-1] += 1

def exibeResultadoVotacao(votos):
  totalVotos = sum(votos)

  if totalVotos == 0:
    print("\n\nNenhum voto foi registrado nesta sessão eleitoral.\n\n")
  else:
    print("\n\nResultado da votação:")
    for i in range(len(votos)):
      print(f"Candidato {i+1}: {votos[i]} votos ({(votos[i]/totalVotos)*100:.2f}%)")
    print(f"Votos nulos: {votos[4]} ({(votos[4]/totalVotos)*100:.2f}%)")
    print(f"Votos em branco: {votos[5]} ({(votos[5]/totalVotos)*100:.2f}%)")

# voto index:[Candidato 1, Candidato 2, Candidato 3, Candidato 4, Candidato 4, nulos, brancos]
votos = [0, 0, 0, 0, 0, 0]

opcoesValidasMenu = [1, 2, 3, 4, 5, 6]

while True:
  exibeopcaoVotos()
  voto, erroTipoVoto, erroVazioVoto, erroMsgVoto = funcoesSuporte.isValidInput("\nDigite a opção para seu voto: ", "int")
  if voto == 0:
    break

  if voto not in opcoesValidasMenu:
    print("\n\nOpção inválida, tente novamente.\n")
    continue
  else:
    registraVotos(voto, votos)

# Ao final exibe os votos e as porcentagens:
exibeResultadoVotacao(votos)
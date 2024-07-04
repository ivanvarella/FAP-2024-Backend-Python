# 3. Investigador Criminal: Crie um programa que faça 5 perguntas para uma pessoa
# sobre um crime:
# * "Telefonou para a vítima?" - Indice: 0
# * "Esteve no local do crime?" - Indice: 1
# * "Mora perto da vítima?" - Indice: 2
# * "Devia para a vítima?" - Indice: 3
# * "Já trabalhou com a vítima?" - Indice: 4

# respostasRecebidas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

# O programa deve classificar a pessoa como:
# * "Inocente": 0-1 respostas positivas
# * "Suspeita": 2 respostas positivas
# * "Cúmplice": 3-4 respostas positivas
# * "Assassino": 5 respostas positivas

import funcoesSuporte as func


respostasPossiveis = ["SIM", "NAO", "NÃO"]

def verificaResposta(resposta):
  if resposta.upper() in respostasPossiveis:
    return True
  else:
    return False

def fazerPerguntas():
  respostasRecebidas = [None] * 5  # Inicializa com 5 elementos None
  
  # "Telefonou para a vítima?" - Indice: 0
  while True:
    resposta, erroTipoResposta, erroVazioResposta, erroMsgResposta = func.isValidInput("Telefonou para a vítima (sim ou não)? ", "string")
    if verificaResposta(resposta):
      respostasRecebidas[0] = resposta.upper()
      break
    else:
      print("As respostas devem ser Sim ou Não.")

  # "Esteve no local do crime?" - Indice: 1
  while True:
    resposta, erroTipoResposta, erroVazioResposta, erroMsgResposta = func.isValidInput("Esteve no local do crime (sim ou não)? ", "string")
    if verificaResposta(resposta):
      respostasRecebidas[1] = resposta.upper()
      break
    else:
      print("As respostas devem ser Sim ou Não.")
  
  # "Mora perto da vítima?" - Indice: 2
  while True:
    resposta, erroTipoResposta, erroVazioResposta, erroMsgResposta = func.isValidInput("Mora perto da vítima (sim ou não)? ", "string")
    if verificaResposta(resposta):
      respostasRecebidas[2] = resposta.upper()
      break
    else:
      print("As respostas devem ser Sim ou Não.")
  
  # "Devia para a vítima?" - Indice: 3
  while True:
    resposta, erroTipoResposta, erroVazioResposta, erroMsgResposta = func.isValidInput("Devia para a vítima (sim ou não)? ", "string")
    if verificaResposta(resposta):
      respostasRecebidas[3] = resposta.upper()
      break
    else:
      print("As respostas devem ser Sim ou Não.")

  # "Já trabalhou com a vítima?" - Indice: 4
  while True:
    resposta, erroTipoResposta, erroVazioResposta, erroMsgResposta = func.isValidInput("Já trabalhou com a vítima (sim ou não)? ", "string")
    if verificaResposta(resposta):
      respostasRecebidas[4] = resposta.upper()
      break
    else:
      print("As respostas devem ser Sim ou Não.")
  return respostasRecebidas

def classificaPessoa(respostasRecebidas):
  numRespostasPositivas = 0
  for resposta in respostasRecebidas:
    if resposta == "SIM":
      numRespostasPositivas += 1

  if numRespostasPositivas <= 1:
    return "Inocente"
  elif numRespostasPositivas == 2:
    return "Suspeita"
  elif numRespostasPositivas >= 3 and numRespostasPositivas <= 4:
    return "Cúmplice"
  else:
    return "Assassino"
  
respostasRecebidas = fazerPerguntas()

#print(f"\nRespostas REcebidas: {respostasRecebidas}")

classificacaoPessoa = classificaPessoa(respostasRecebidas)

print(f"\n\nA pessoa foi classificada como: {classificacaoPessoa}.\n")
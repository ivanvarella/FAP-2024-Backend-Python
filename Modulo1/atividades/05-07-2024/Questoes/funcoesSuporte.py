import json
import os

# Caminho do diretório atual
caminho = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/"

# Futuros aprimoramentos:
# 1- Função isValid:
#   - Receber listas e realizar validações
#   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções a fins
#   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos
# Função para validação de entradas input
# - msg: mensagem mostrada no input
# - tipoEsperado: "string", "int", "float", "intFloat" - "intFloat" podendo receber int ou float
# - aceitaVazio: padrão False (não aceitando valors vazios), caso aceite, declarar na chamada da função como True
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

# ############################ CRUD Json ############################
#Funções CRUD (Create, Read, Update, Delete):

# ---------------------------------------------------------------------------
# Função Create - Funcionando corretamente:
def createAluno(novoAluno, arquivoJson):
  # Caminho do arquivo JSON
  global caminho  # Declarar que vamos usar a variável global 'caminho'
  caminhoCompleto = os.path.join(caminho, arquivoJson)

  # Carregar dados do arquivo JSON
  with open(caminhoCompleto, 'r', encoding='utf-8') as f:
    data = json.load(f)

  # Se o Json vazio, inicializa-o como objeto 'Alunos'
  if 'Alunos' not in data:
    data['Alunos'] = []
  
  # Determinar o próximo ID único e sequencial:
  ids = []
  # Percorra cada aluno na lista 'data["Alunos"]' e adicione o ID do aluno à lista 'ids'
  for aluno in data["Alunos"]:
    ids.append(aluno["id"])
  # Encontre o maior ID e adicionar 1 para gerar o novo ID
  novo_id = max(ids) + 1
  # Adiciona ao aluno que será gravado no Json com ID novo
  novoAluno["id"] = novo_id

  # Adicionar novo Aluno ao cadastro
  data['Alunos'].append(novoAluno)

  # Escrever de volta no arquivo JSON
  with open(caminhoCompleto, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------

# Função Read - Funcionanado corretamente:
def readAlunos(arquivoJson):
  # Caminho do arquivo JSON
  global caminho  # Declarar que vamos usar a variável global 'caminho'
  caminhoCompleto = os.path.join(caminho, arquivoJson)
    
  # Carregar dados do arquivo JSON
  with open(caminhoCompleto, 'r', encoding='utf-8') as f:
      data = json.load(f)
  
  return data
# ---------------------------------------------------------------------------

# Função Update - Falta testar:
# Fluxo: Read data -> Encontra o aluno pelo id -> Atualiza o aluno no dicionário obtino no Read
# -> Salvar o novo Json com o aluno atualizado (todo o Json é gravado).
def updateAluno(alunoId, novosDados, arquivoJson):
  data = readAlunos(arquivoJson)
  if "Alunos" not in data:
    print("Nenhum aluno cadastrado no sistema.")
    return
  alunoEncontrado = False
  for i, aluno in enumerate(data["Alunos"]):
    if aluno["id"] == alunoId:
      alunoEncontrado = True
      data["Alunos"][i].update(novosDados) # método update: atualiza dados dicionário
      break
  if alunoEncontrado:
    # Caminho do arquivo JSON
    global caminho  # Declarar que vamos usar a variável global 'caminho'
    caminhoCompleto = os.path.join(caminho, arquivoJson)

    with open(caminhoCompleto, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Aluno com ID {alunoId} atualizado com sucesso.")
  else:
    print(f"Aluno com ID {alunoId} não encontrado.")

# ---------------------------------------------------------------------------
# Função Delete - Funcionando corretamente:
# Fluxo: Read data -> Encontra o aluno pelo id -> Apaga aluno no dicionário obtino no Read
# -> Salvar o novo Json com o aluno excluído.
# Função para deletar aluno pelo ID
def deleteAluno(alunoId, arquivoJson):
  # Carregar dados do arquivo JSON
  data = readAlunos(arquivoJson)

  # Se o Json vazio, inicializa-o como objeto 'Alunos'
  if "Alunos" not in data:
    print("Nenhum aluno cadastrado no sistema.")
    return

  # Encontrar o aluno pelo ID e remover do dicionário carregado previamente (data)
  alunoEncontrado = False
  # Pega valor-chave (i, aluno), onde i = index e aluno = dicionário com os dados de cada aluno
  for i, aluno in enumerate(data["Alunos"]):
    if aluno["id"] == alunoId:
      alunoEncontrado = True
      # Pega os dados do aluno antes de deletar para poder mostrar na tela
      nomeAlunoDeletado = data["Alunos"][i]["nome"]
      matriculaAlunoDeletado = data["Alunos"][i]["matricula"]
      idAlunoDeletado = data["Alunos"][i]["id"]
      # Deleção de um único aluno via index
      del data["Alunos"][i] 
      break # Encontrou -> interrompe o for

  if alunoEncontrado:
    # Caminho do arquivo JSON
    global caminho  # Declarar que vamos usar a variável global 'caminho'
    caminhoCompleto = os.path.join(caminho, arquivoJson)

    # Escreve de volta no JSON, o arquivo completo com todos os alunos, menos o aluno deletado
    with open(caminhoCompleto, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"O Aluno {nomeAlunoDeletado} (Id: {idAlunoDeletado} / Matrícula: {matriculaAlunoDeletado}) foi deletado com sucesso.")
  else:
    print(f"Aluno com ID {alunoId} não encontrado.")
  # ---------------------------------------------------------------------------
  
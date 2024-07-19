import json
import os

# Caminho do diretório atual
# os.getcwd() -> /home/ivanvarella/dev/FAP/FAP-2024-Backend-Python
caminhoPastaPadrao = os.getcwd()
caminho = os.path.join(caminhoPastaPadrao, "Modulo1", "projetos", "Atividade_avaliacao1", "cadAlunosSys")

## Função exibir menu opções:
def exibirMenuPrincipal():
    print("\n\n########### Menu Principal ############")
    print("#                                     #")
    print("#   Cod[1]: Cadastrar Aluno           #")
    print("#   Cod[2]: Listar / Alterar Alunos   #")
    print("#   Cod[3]: Pesquisar                 #")
    print("#   Cod[4]: Sair                      #")
    print("#                                     #")
    print("#   Cod[5]: Sobre                     #")
    print("#                                     #")
    print("#######################################\n")
    # Verifica erros de tipo: Erros: Vazio, string, float
    opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu = isValidInput("Digite a opção desejada: ", "int")
    return opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu

## Função exibir Sobre:
def sobre():
    print("\n\n################# Sobre #######################")
    print("#                                             #")
    print("# Bem-vindo ao Sistema de Cadastro de Alunos  #")
    print("# Atividade do curso FAP Softex 2024 - Natal  #")
    print("# Desenvolvedores:                            #")
    print("#  - Ivan Varella                             #")
    print("#  - Ricardo Nogueira                         #") 
    print("# Data: 18/07/2024                            #")
    print("# Versão: 1.0.1                               #")
    print("#                                             #")
    print("###############################################\n")
    opcaoSobre, erroTipoSobre, erroVazioSobre, erroMsgSobre = isValidInput("Digite Enter para voltar: ", "string", True) # Aceita vazio, o usuário só pressiona o Enter e volta

## Função de opções mostrada dentro do Exibir alunos - Exibe e depois manipula os alunos
def exibirMenuAlterarExcluir():
    print("\n\n################################")
    print("# Menu Alterar/ Excluir Aluno  #")
    print("#                              #")
    print("#   Cod[1]: Alterar Cadastro   #")
    print("#   Cod[2]: Excluir Cadastro   #")
    print("#   Cod[3]: Voltar             #")
    print("#                              #")
    print("################################\n")

## Função Sair:
def sair():
    print("\n\n#########################################################")
    print("#  Obrigado por usar o Sistema de Cadastro de Alunos    #")
    print("#########################################################\n\n")

## Função calcular média notas aluno
def calcularMediaNotas(notasAluno):
  if len(notasAluno) == 0:
    return 0
  else:
    return sum(notasAluno) / len(notasAluno)

## Função listar alunos cadastrados
def listarAlunos():
  dados = readAlunos("alunos.json")
  alunos = dados.get("Alunos", [])  # get(): Pega valores da chave 'Alunos' no dicionário, caso não exista a chave, retorna vazio
  
  # Se não tiver alunos
  if len(alunos) == 0:
      print("\n\nNenhum aluno cadastrado.\n\n")
      return

  # Mostrando alunos cadastrados
  print("\n\n############# Lista de Alunos #############")
  print(f"Total de alunos cadastrados: {len(alunos)}")
  for aluno in alunos:
    
    mediaNotas = calcularMediaNotas(aluno["notas"])

    print(f"\nMatrícula: {aluno['matricula']}")
    print(f'Nome: {aluno["nome"]}')
    print(f'Curso: {aluno["curso"]}')
    print(f'Notas: {", ".join(map(str, aluno["notas"]))}')  # ', '.join(...): Une strings em única string, separando por ', '.
    print(f'Média das notas: {mediaNotas:.1f}')
    print(f'Presenças: {aluno["presencas"]}')
    print(f'Telefone: {aluno["telefone"]}')
    print(f'Email: {aluno["email"]}')
    print("-" * 30)
  
  # Opção alterar ou excluir aluno dentro de listar, para facilitar, já que o usuário poderá 
  # visualizar os alunos antes de realizar as alterações:
  exibirMenuAlterarExcluir()
  opcaoMenuAlterarExcluir, erroTipoOpcaoMenuAlterarExcluir, erroVazioOpcaoMenuAlterarExcluir, erroMsgOpcaoMenuAlterarExcluir = isValidInput("Digite a opção desejada: ", "int")
  # Controla os opções do Menu Alterar / Excluir aluno
  if opcaoMenuAlterarExcluir == 3:
      return opcaoMenuAlterarExcluir
  elif opcaoMenuAlterarExcluir == 1:
      alterarAluno()
  elif opcaoMenuAlterarExcluir == 2:
      excluirAluno()
  else:
      print("\nOpção inválida!\n")
  
## Exibir Menu Pesquisar
def exibirMenuPesquisarCriterio():
    print("\n\n#######  Menu Pesquisar  #######")
    print("#                              #")
    print("#   Cod[1]: Por Nome           #")
    print("#   Cod[2]: Por Matrícula      #")
    print("#   Cod[3]: Por E-mail         #")
    print("#   Cod[4]: Por Curso          #")
    print("#                              #")
    print("################################\n")
    # Verifica a opção digitada e trata
    while True:
      criterio, erroTipoCriterio, erroVazioCriterio, erroMsgCriterio = isValidInput("Digite a opção desejada: ", "int")
      if criterio not in [1, 2, 3, 4, 5]:  # Corrigido de "is not in" para "not in"
        print("Opção inválida.")
      else:
        break
    return criterio

## Função para pesquisar nome = 1 / matrícula = 2 / email = 3 / curso = 4
def pesquisar():
  # Exibir menu principal da pesquisa + obter o critério da pesquisa
  criterio = exibirMenuPesquisarCriterio()

  # Obtém o valor a ser pesquisado
  if criterio == 1:
     valorBusca, erroTipoValorBusca, erroVazioValorBusca, erroMsgValorBusca = isValidInput("Digite o nome a ser pesquisado: ", "string")
     nomeCriterio = "Nome"
  elif criterio == 2:
     valorBusca, erroTipoValorBusca, erroVazioValorBusca, erroMsgValorBusca = isValidInput("Digite a matrícula a ser pesquisada: ", "int")
     nomeCriterio = "Matrícula"
  elif criterio == 3:
     valorBusca, erroTipoValorBusca, erroVazioValorBusca, erroMsgValorBusca = isValidInput("Digite o e-mail a ser pesquisado: ", "string")
     nomeCriterio = "E-mail"
  elif criterio == 4:
     valorBusca, erroTipoValorBusca, erroVazioValorBusca, erroMsgValorBusca = isValidInput("Digite o curso a ser pesquisado: ", "string")
     nomeCriterio = "Curso"

  # Obtém os dados do Json com a mesma estrutura
  dados = readAlunos("alunos.json")
  # Trata os dados pegando os valores da chave alunos e criando 
  # # uma lista de dicionários, onde cada dicionário é um aluno
  alunos = dados.get("Alunos", [])
  resultados = []

  # Percorre todo o Json acumulando (qnd mais de 1 resultado) os dados completos daquele aluno
  for aluno in alunos:
    if criterio == 1 and valorBusca.lower() in aluno["nome"].lower():
      resultados.append(aluno)
    elif criterio == 2 and valorBusca == aluno["matricula"]:
      resultados.append(aluno)
    elif criterio == 3 and valorBusca.lower() in aluno["email"].lower():
      resultados.append(aluno)
    elif criterio == 4 and valorBusca.lower() in aluno["curso"].lower():
      resultados.append(aluno)

  # Se não retornar vazio, mostra os alunos cujo critério deu certo
  if resultados:
    print(f"\n{len(resultados)} aluno(s) encontrado(s) com {nomeCriterio} '{valorBusca}':")
    for aluno in resultados:

      mediaNotas = calcularMediaNotas(aluno["notas"])

      print(f"\nMatrícula: {aluno['matricula']}")
      print(f'Nome: {aluno["nome"]}')
      print(f'Curso: {aluno["curso"]}')
      print(f'Notas: {", ".join(map(str, aluno["notas"]))}')
      print(f'Média das notas: {mediaNotas:.1f}')
      print(f'Presenças: {aluno["presencas"]}')
      print(f'Telefone: {aluno["telefone"]}')
      print(f'Email: {aluno["email"]}')
      print("-" * 30)
  else:
    print(f"\nNenhum aluno encontrado com {nomeCriterio} '{valorBusca}'.")


## Função excluir aluno (dentro do Listar Alunos):
def excluirAluno():
  idAlunoExcluir, erroTipoIdAlunoExcluir, erroVazioIdAlunoExcluir, erroMsgIdAlunoExcluir = isValidInput("Digite a matrícula do aluno a ser excluido: ", "int")
  deleteAluno(idAlunoExcluir, "alunos.json")

## Função alterar aluno (dentro do Listar Alunos):
def alterarAluno():
  matriculaAlunoAlterar, erroTipoMatriculaAlunoAlterar, erroVazioMatriculaAlunoAlterar, erroMsgMatriculaAlunoAlterar = isValidInput("Digite a matrícula do aluno a ser alterado: ", "int")

  # Carrega Json
  dados = readAlunos("alunos.json")
  alunos = dados.get("Alunos", [])
  # Flag
  achoAluno = False
  for aluno in alunos:
    if aluno["matricula"] == matriculaAlunoAlterar:
      achoAluno = True

      mediaNotas = calcularMediaNotas(aluno["notas"])

      # Mostra os dados atuais do aluno encontrado:
      print("\n############# Dados Atuais do Aluno #############")
      print(f"\nMatrícula: {aluno['matricula']}")
      print(f'Nome: {aluno["nome"]}')
      print(f'Curso: {aluno["curso"]}')
      print(f'Notas: {", ".join(map(str, aluno["notas"]))}')
      print(f'Média das notas: {mediaNotas:.1f}')
      print(f'Presenças: {aluno["presencas"]}')
      print(f'Telefone: {aluno["telefone"]}')
      print(f'Email: {aluno["email"]}')
      print("-" * 30)
      break
  if not achoAluno:
    print("\n\nAluno não encontrado.\n\n")
    # Retorna e não faz a atualização - Early return pattern
    return

  # Pega os novos dados do aluno (menos id e matrícula que não mudam em relação ao aluno)
  novosDados = obterNovosDadosAluno()
  updateAluno(matriculaAlunoAlterar, novosDados, "alunos.json")

## Função para "pegar" os novos dados do aluno a ser atualizado
def obterNovosDadosAluno():
  novosDados = {}

  novosDados['nome'], erroTipoNovoNome, erroVazioNovoNome, erroMsgNovoNome = isValidInput("Digite o novo nome do aluno: ", "string")
  novosDados['curso'], erroTipoNovoCurso, erroVazioNovoCurso, erroMsgNovoCurso = isValidInput("Digite o novo curso do aluno: ", "string")
  novosDados['presencas'], erroTipoNovasPresencas, erroVaziasNovasPresencas, erroMsgNovasPresencas = isValidInput("Digite o novo número de presenças do aluno: ", "int")
  novosDados['telefone'], erroTipoNovoTelefone, erroVazioNovoTelefone, erroMsgNovoTelefone = isValidInput("Digite o novo telefone do aluno: ", "string")
  novosDados['email'], erroTipoNovoEmail, erroVazioNovoEmail, erroMsgNovoEmail = isValidInput("Digite o novo email do aluno: ", "string")
  
  # Entrada das notas do aluno:
  novosDados['notas'] = trataNotasAluno() # Exemplo de retorno: [9.5, 6.5, 8.2]

  return novosDados

## Função exibir tela de cadastro novo aluno:
def telaCadastroAluno():
    print("\n\n############# Cadastro de Aluno #############")

    # Preparação dados:
    novoAluno = {}

    novoAluno['matricula'] = None #Inicializando a matrícula, que será incrementada e inserida automaticamente ao cadastro do aluno
    novoAluno['nome'], erroTipoNomeAluno, erroVazioNomeAluno, erroMsgNomeAluno = isValidInput("Digite o nome do aluno: ", "string")
    novoAluno['curso'], erroTipoCursoAluno, erroVazioCursoAluno, erroMsgCursoAluno = isValidInput("Digite o curso: ", "string")
    novoAluno['presencas'], erroTipoPresencas, erroVazioPresencas, erroMsgPresencas = isValidInput("Digite o número de presenças: ", "int")
    novoAluno['telefone'], erroTipoTelefone, erroVazioTelefone, erroMsgTelefone = isValidInput("Digite o telefone: ", "string")
    novoAluno['email'], erroTipoEmail, erroVazioEmail, erroMsgEmail = isValidInput("Digite o email: ", "string")
    # Entrada das notas do aluno:
    novoAluno['notas'] = trataNotasAluno() # Exemplo de retorno: [9.5, 6.5, 8.2]

    # Create no Json
    try:
      createAluno(novoAluno, "alunos.json")
      print("\n\n########################### Aluno cadastrado com sucesso! ###########################\n")
    except Exception as e:
      print(f"Erro ao criar o aluno: {e}")
      
## Função utilizada tratar notas no momento do cadastro do aluno:
def trataNotasAluno():
  numNotas, erroTipoNumNotas, erroVazioNumNotas, erroMsgNumNotas = isValidInput("Informe o número de notas a serem cadastradas: ", "int")
  notas = []
  for i in range(numNotas):
    while True:
      nota, erroTipoNota, erroVazioNota, erroMsgNota = isValidInput(f"Informe a {i+1}ª nota: ", "float")
      if 0 <= nota <= 10:  # Verifica se a nota está entre 0 e 10
        notas.append(nota)
        break
      else:
        print("A nota deve estar entre 0 e 10.")
  return notas

## Função para validação de entradas input
# - msg: mensagem mostrada no input
# - tipoEsperado: "string", "int", "float", "intFloat" - "intFloat" podendo receber int ou float
# - aceitaVazio: padrão False (não aceitando valors vazios), caso aceite, declarar na chamada da função como True
# - Retorno da função: valor, erroTipo, erroVazio, msgErro
def isValidInput(msg, tipoEsperado, aceitaVazio = False):

  # Futuros aprimoramentos:
  # 1- Função isValid:
  #   - Receber listas e realizar validações
  #   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções a fins
  #   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos


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
## Função Create - Funcionando corretamente:
def createAluno(novoAluno, arquivoJson):
  # Caminho do arquivo JSON
  global caminho  # Declarar que vamos usar a variável global 'caminho'
  caminhoCompleto = os.path.join(caminho, arquivoJson)

  # Carregar dados do arquivo JSON
  with open(caminhoCompleto, 'r', encoding='utf-8') as f:
    data = json.load(f)

  # Se o Json estiver vazio, inicializa-o como objeto 'Alunos'
  if 'Alunos' not in data:
    data['Alunos'] = []
  
  # Determinar a próxima Matrícula única e sequencial:
  matriculas = []
  # Percorra cada aluno na lista 'data["Alunos"]' e adicione a matrícula do aluno à lista 'matriculas'
  for aluno in data["Alunos"]:
    matriculas.append(aluno["matricula"])
  # Encontre a maior Matrícula e adiciona 1 para gerar a nova Matrícula
  nova_matricula = max(matriculas) + 1
  # Adiciona ao aluno que será gravado no Json com a Matrícula nova
  novoAluno["matricula"] = nova_matricula

  # Adicionar novo Aluno ao cadastro
  data['Alunos'].append(novoAluno)

  # Escrever de volta no arquivo JSON
  with open(caminhoCompleto, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------

## Função Read - Funcionanado corretamente:
def readAlunos(arquivoJson):
  # Caminho do arquivo JSON
  global caminho  # Declarar que vamos usar a variável global 'caminho'
  caminhoCompleto = os.path.join(caminho, arquivoJson)
    
  # Carregar dados do arquivo JSON
  with open(caminhoCompleto, 'r', encoding='utf-8') as f:
      data = json.load(f)
  
  return data
# ---------------------------------------------------------------------------

## Função Update - funcionando:
# Fluxo: Read data -> Encontra o aluno pelo id -> Atualiza o aluno no dicionário obtino no Read
# -> Salvar o novo Json com o aluno atualizado (todo o Json é gravado).
def updateAluno(alunoMatricula, novosDados, arquivoJson):
  data = readAlunos(arquivoJson)
  if "Alunos" not in data:
    print("Nenhum aluno cadastrado no sistema.")
    return
  alunoEncontrado = False
  for i, aluno in enumerate(data["Alunos"]):
    if aluno["matricula"] == alunoMatricula:
      alunoEncontrado = True
      # Método update: atualiza dados no dicionário passado na posição do index
      # como só tem uma matrícula, então só altera esta.
      data["Alunos"][i].update(novosDados)
      break
  if alunoEncontrado:
    # Caminho do arquivo JSON
    global caminho  # Declarar que vamos usar a variável global 'caminho'
    caminhoCompleto = os.path.join(caminho, arquivoJson)

    with open(caminhoCompleto, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nAluno com Matrícula {alunoMatricula} atualizado com sucesso.")
  else:
    print(f"Aluno com Matrícula {alunoMatricula} não encontrado.")

# ---------------------------------------------------------------------------
## Função Delete - Funcionando corretamente:
# Fluxo: Read data -> Encontra o aluno pelo id -> Apaga aluno no dicionário obtino no Read
# -> Salvar o novo Json com o aluno excluído.
# Função para deletar aluno pelo ID
def deleteAluno(alunoMatricula, arquivoJson):
  # Carregar dados do arquivo JSON
  data = readAlunos(arquivoJson)

  # Se o Json vazio, msg de "warning"
  if "Alunos" not in data:
    print("Nenhum aluno cadastrado no sistema.")
    return

  # Encontrar o aluno pela Matrícula e remover do dicionário carregado previamente (data)
  alunoEncontrado = False
  # Pega valor-chave (i, aluno), onde i = index e aluno = dicionário com os dados de cada aluno
  for i, aluno in enumerate(data["Alunos"]):
    if aluno["matricula"] == alunoMatricula:
      alunoEncontrado = True
      # Pega os dados do aluno antes de deletar para poder mostrar na tela
      nomeAlunoDeletado = data["Alunos"][i]["nome"]
      matriculaAlunoDeletado = data["Alunos"][i]["matricula"]
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
    print(f"O Aluno {nomeAlunoDeletado} (Matrícula: {matriculaAlunoDeletado}) foi deletado com sucesso.")
  else:
    print(f"Aluno com a Matrícula {alunoMatricula} não foi encontrado.")
  # ---------------------------------------------------------------------------
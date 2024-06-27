import json
import os

# Caminho do diretório atual
caminho = os.getcwd() + "/Modulo1/atividades/26-06-2024/cadAlunosSys/"


# Função exibir menu opções:
def exibirMenuPrincipal():
    print("\n\n######## Menu Principal ########")
    print("#                              #")
    print("#   Cod[1]: Cadastrar Aluno    #")
    print("#   Cod[2]: Listar Alunos      #")
    print("#   Cod[3]: Sair               #")
    print("#   Cod[4]: Sobre              #")
    print("#                              #")
    print("################################\n")
    # Verifica erros de tipo: Erros: Vazio, string, float
    opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu = isValidInput("Digite a opção desejada: ", "int")
    return opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu

# Função exibir Sobre:
def sobre():
    print("\n\n################# Sobre #######################")
    print("#                                             #")
    print("# Bem-vindo ao Sistema de Cadastro de Alunos  #")
    print("# Atividade do curso FAP Softex 2024 - Natal  #")
    print("# Desenvolvedor: Ivan Varella                 #")
    print("# Data: 26/06/2024                            #")
    print("# Versão: 1.0                                 #")
    print("#                                             #")
    print("###############################################\n")
    opcaoSobre, erroTipoSobre, erroVazioSobre, erroMsgSobre = isValidInput("Digite Enter para voltar: ", "string", True) # Aceita vazio, o usuário só pressiona o Enter e volta

def exibirMenuAlterarExcluir():
    print("\n\n# Menu Alterar/ Excluir Aluno  #")
    print("#                              #")
    print("#   Cod[1]: Alterar Cadastro   #")
    print("#   Cod[2]: Excluir Cadastro   #")
    print("#   Cod[3]: Voltar             #")
    print("#                              #")
    print("################################\n")

# Função Sair:
def sair():
    print("\n\nObrigado por usar o Sistema de Cadastro de Alunos!\n\n")

# Função listar alunos cadastrados
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
        print(f"\nID: {aluno['id']}")
        print(f'Nome: {aluno["nome"]}')
        print(f'Curso: {aluno["curso"]}')
        print(f'Matrícula: {aluno["matricula"]}')
        print(f'Notas: {", ".join(map(str, aluno["notas"]))}')  # ', '.join(...): Une strings em única string, separando por ', '.
        print(f'Presenças: {aluno["presencas"]}')
        print(f'Telefone: {aluno["telefone"]}')
        print(f'Email: {aluno["email"]}')
        print("-" * 30)
    
    # Opção alterar ou excluir aluno:
    exibirMenuAlterarExcluir()
    opcaoMenuAlterarExcluir, erroTipoOpcaoMenuAlterarExcluir, erroVazioOpcaoMenuAlterarExcluir, erroMsgOpcaoMenuAlterarExcluir = isValidInput("Digite a opção desejada: ", "int")
    # Controla os opções do Menu Alterar / Excluir aluno
    if opcaoMenuAlterarExcluir == 3:
       return opcaoMenuAlterarExcluir
    elif opcaoMenuAlterarExcluir == 1:
        #alterarAluno()
        print("\nAlterar Aluno: Ainda não implementado!\n")
    elif opcaoMenuAlterarExcluir == 2:
        #excluirAluno()
        print("\nExcluir Aluno: Ainda não implementado!\n")
    else:
        print("\nOpção inválida!\n")
       


# Função exibir tela de cadastro novo aluno:
def telaCadastroAluno():
    print("\n\n############# Cadastro de Aluno #############")

    # Preparação dados:
    novoAluno = {}

    novoAluno['id'] = None #Inicializando o id
    novoAluno['nome'], erroTipoNomeAluno, erroVazioNomeAluno, erroMsgNomeAluno = isValidInput("Digite o nome do aluno: ", "string")
    novoAluno['curso'], erroTipoCursoAluno, erroVazioCursoAluno, erroMsgCursoAluno = isValidInput("Digite o curso: ", "string")
    novoAluno['matricula'], erroTipoMatricula, erroVazioMatricula, erroMsgMatricula = isValidInput("Digite a matrícula: ", "int")
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
      
# Função utilizada tratar notas no momento do cadastro do aluno:
def trataNotasAluno():
  numNotas, erroTipoNumNotas, erroVazioNumNotas, erroMsgNumNotas = isValidInput("Informe o número de notas a serem cadastradas: ", "int")
  notas = []
  for i in range(numNotas):
    nota, erroTipoNota, erroVazioNota, erroMsgNota = isValidInput(f"Informe a {i+1}ª nota: ", "float")
    notas.append(nota)
  return notas




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

# -------------------------- CRUD Json ----------------------------------
#Funções CRUD (Create, Read, Update, Delete):

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

# Função Read - Funcionanado corretamente:
def readAlunos(arquivoJson):
  # Caminho do arquivo JSON
  global caminho  # Declarar que vamos usar a variável global 'caminho'
  caminhoCompleto = os.path.join(caminho, arquivoJson)
    
  # Carregar dados do arquivo JSON
  with open(caminhoCompleto, 'r', encoding='utf-8') as f:
      data = json.load(f)
  
  return data



  # Função Update - Falta Fazer:

  # Função Delete - Falta Fazer:


  # ---------------------------------------------------------------------------
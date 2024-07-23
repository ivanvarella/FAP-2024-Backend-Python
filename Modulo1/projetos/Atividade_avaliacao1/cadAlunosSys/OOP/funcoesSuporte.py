import os
from alunos import Aluno
from jsonHandler import JsonHandler
from copy import deepcopy

# Caminho do diretório atual
caminhoPastaPadrao = os.getcwd()
caminho = os.path.join(
    caminhoPastaPadrao,
    "Modulo1",
    "projetos",
    "Atividade_avaliacao1",
    "cadAlunosSys",
    "OOP",
)


## Função exibir menu opções:
def exibirMenuPrincipal():
    print("\n\n########### Menu Principal ############")
    print("#            [ Alunos ]               #")
    print("#                                     #")
    print("#   Cod[1]: Cadastrar Aluno           #")
    print("#   Cod[2]: Listar / Alterar Aluno    #")
    print("#   Cod[3]: Pesquisar Aluno           #")
    print("# ----------------------------------- #")
    print("#          [ Professores ]            #")
    print("#                                     #")
    print("#   Cod[4]: Cadastrar Professor       #")
    print("#   Cod[5]: Listar / Alterar Prof.    #")
    print("#   Cod[6]: Pesquisar Professor       #")
    print("# ----------------------------------- #")
    print("#         [ Outras opções ]           #")
    print("#                                     #")
    print("#   Cod[7]: Listar                    #")
    print("#   Cod[8]: Pesquisar                 #")
    print("# ----------------------------------- #")
    print("#                                     #")
    print("#   Cod[9]: Sair                      #")
    print("#   Cod[0]: Sobre                     #")
    print("#                                     #")
    print("#######################################\n")
    # Verifica erros de tipo: Erros: Vazio, string, float
    (opcaoMenuPrincipal, _, _, _) = isValidInput("Digite a opção desejada: ", "int")
    return opcaoMenuPrincipal


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
    opcaoSobre, _, _, _ = isValidInput(
        "Digite Enter para voltar: ", "string", True
    )  # Aceita vazio, o usuário só pressiona o Enter e volta


## Função de opções mostrada dentro do Exibir alunos - Exibe e depois manipula os alunos
def exibirMenuAlterarExcluir(chaveJson):
    if chaveJson == "Alunos":
        print("\n\n################################")
        print("# Menu Alterar/ Excluir Aluno  #")
        print("#                              #")
        print("#   Cod[1]: Alterar Cadastro   #")
        print("#   Cod[2]: Excluir Cadastro   #")
        print("#   Cod[3]: Voltar             #")
        print("#                              #")
        print("################################\n")
        (
            opcaoMenuAlterarExcluir,
            _,
            _,
            _,
        ) = isValidInput("Digite a opção desejada: ", "int")
        return opcaoMenuAlterarExcluir
    elif chaveJson == "Professores":
        print("\n\n#####################################")
        print("#  Menu Alterar/ Excluir Professor  #")
        print("#                                   #")
        print("#   Cod[1]: Alterar Cadastro        #")
        print("#   Cod[2]: Excluir Cadastro        #")
        print("#   Cod[3]: Voltar                  #")
        print("#                                   #")
        print("#####################################\n")
        (
            opcaoMenuAlterarExcluir,
            _,
            _,
            _,
        ) = isValidInput("Digite a opção desejada: ", "int")
        return opcaoMenuAlterarExcluir
    else:
        (
            opcaoMenuAlterarExcluir,
            _,
            _,
            _,
        ) = isValidInput("Digite Enter para voltar: ", "string", aceitaVazio=True)
        return


## Função Sair:
def sair():
    print("\n\n#########################################################")
    print("#  Obrigado por usar o Sistema de Cadastro de Alunos    #")
    print("#########################################################\n\n")


## Exibir Menu Pesquisar
def exibirMenuPesquisarCriterio(chaveJson):
    if chaveJson == "Alunos":
        print("\n\n#######  Menu Pesquisar  #######")
        print("#                              #")
        print("#   Cod[1]: Por Nome           #")
        print("#   Cod[2]: Por Matrícula      #")
        print("#   Cod[3]: Por E-mail         #")
        print("#   Cod[4]: Por Curso          #")
        print("#                              #")
        print("################################\n")
    elif chaveJson == "Professores":
        print("\n\n#######  Menu Pesquisar  #######")
        print("#                              #")
        print("#   Cod[1]: Por Nome           #")
        print("#   Cod[2]: Por Matrícula      #")
        print("#   Cod[3]: Por E-mail         #")
        print("#   Cod[4]: Disciplina         #")
        print("#                              #")
        print("################################\n")
    elif chaveJson == "":
        print("\n\n#######  Menu Pesquisar  #######")
        print("#                              #")
        print("#   Cod[1]: Por Nome           #")
        print("#   Cod[2]: Por Matrícula      #")
        print("#   Cod[3]: Por E-mail         #")
        print("#                              #")
        print("################################\n")

    # Verifica a opção digitada e trata
    while True:
        criterio, _, _, _ = isValidInput("Digite a opção desejada: ", "int")

        opcoes_validas = {
            "Alunos": [1, 2, 3, 4],
            "Professores": [1, 2, 3, 4],
            "": [1, 2, 3],
        }

        # Obtem o valor da chave correspondente ao valor de chaveJson no dicionário opcoes_validas
        if criterio in opcoes_validas.get(chaveJson, []):
            return criterio
        else:
            print("Opção inválida.")


## Função listar dados cadastrados
# Para listar, só é preciso instanciar a classe JsonHandler.
def listar(chaveJson=""):

    # Cria uma instância de JsonHandler
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acodor com o retorno do chaveJson
    dados = json_handler.read()
    # get(): Pega valores da chave 'Alunos' no dicionário, caso não exista a chave, retorna vazio
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])

    # Se tiver buscado por Alunos e não existir nenhum
    if chaveJson == "Alunos" and len(alunos) == 0:
        print("\n\nNenhum Aluno cadastrado.\n\n")
        return

    # Se tiver buscado por Professores e não existir nenhum
    if chaveJson == "Professores" and len(professores) == 0:
        print("\n\nNenhum Professor cadastrado.\n\n")
        return

    # Se tiver buscado por Dados e não existir nenhum
    if chaveJson == "" and len(dados) == 0:
        print("\n\nNenhum Aluno cadastrado.\n\n")
        return

    # Mostrando Alunos cadastrados
    if chaveJson == "Alunos" or chaveJson == "":
        print("\n\n############# Lista de Alunos #############")
        print(f"Total de alunos cadastrados: {len(alunos)}")
        for aluno in alunos:

            # Usa o método estático da classe Aluno para calcular a média
            mediaNotas = Aluno.calcular_media(aluno["notas"])

            print(f"\nMatrícula: {aluno['matricula']}")
            print(f'Nome: {aluno["nome"]}')
            print(f'Curso: {aluno["curso"]}')
            print(
                f'Notas: {", ".join(map(str, aluno["notas"]))}'
            )  # ', '.join(...): Une strings em única string, separando por ', '.
            print(f"Média das notas: {mediaNotas:.1f}")
            print(f'Presenças: {aluno["presencas"]}')
            print(f'Telefone: {aluno["telefone"]}')
            print(f'Email: {aluno["email"]}')
            print("-" * 30)

    # Mostrando Professores cadastrados
    if chaveJson == "Professores" or chaveJson == "":
        print("\n\n############# Lista de Professores #############")
        print(f"Total de Professores cadastrados: {len(professores)}")
        for professor in professores:

            print(f"\nMatrícula: {professor['matricula']}")
            print(f'Nome: {professor["nome"]}')
            print(f'Disciplinas: {professor["disciplinas"]}')
            print(f'Turmas: {professor["turmas"]}')
            print(f'Telefone: {professor["telefone"]}')
            print(f'Email: {professor["email"]}')
            print("-" * 30)

    # Opção alterar ou excluir aluno ou professor dentro de listar, para facilitar,
    # já que o usuário poderá visualizar os alunos antes de realizar as alterações:
    opcaoMenuAlterarExcluir = exibirMenuAlterarExcluir(chaveJson)

    # Controla os opções do Menu Alterar / Excluir aluno
    if opcaoMenuAlterarExcluir == 3:
        return  # Volta para o o loop do menu principal
    elif opcaoMenuAlterarExcluir == 1:
        alterar(chaveJson)
    elif opcaoMenuAlterarExcluir == 2:
        excluir(chaveJson)
    else:
        print("\nOpção inválida!\n")


## Função para pesquisar nome = 1 / matrícula = 2 / email = 3 / curso = 4
def pesquisar(chaveJson=""):
    print("Revisar função pesquisar...")

    # Exibir menu principal da pesquisa + obter o critério da pesquisa
    criterio = exibirMenuPesquisarCriterio(chaveJson)

    # Obtém o valor a ser pesquisado
    if chaveJson == "Alunos":
        if criterio == 1:
            valorBusca, _, _, _ = isValidInput(
                "Digite o nome a ser pesquisado: ", "string"
            )
            nomeCriterio = "Nome"
        elif criterio == 2:
            valorBusca, _, _, _ = isValidInput(
                "Digite a matrícula a ser pesquisada: ", "int"
            )
            nomeCriterio = "Matrícula"
        elif criterio == 3:
            valorBusca, _, _, _ = isValidInput(
                "Digite o e-mail a ser pesquisado: ", "string"
            )
            nomeCriterio = "E-mail"
        elif criterio == 4:
            valorBusca, _, _, _ = isValidInput(
                "Digite o curso a ser pesquisado: ", "string"
            )
            nomeCriterio = "Curso"
    elif chaveJson == "Professores":
        if criterio == 1:
            valorBusca, _, _, _ = isValidInput(
                "Digite o nome a ser pesquisado: ", "string"
            )
            nomeCriterio = "Nome"
        elif criterio == 2:
            valorBusca, _, _, _ = isValidInput(
                "Digite a matrícula a ser pesquisada: ", "int"
            )
            nomeCriterio = "Matrícula"
        elif criterio == 3:
            valorBusca, _, _, _ = isValidInput(
                "Digite o e-mail a ser pesquisado: ", "string"
            )
            nomeCriterio = "E-mail"
        elif criterio == 4:
            valorBusca, _, _, _ = isValidInput(
                "Digite a disciplina a ser pesquisada: ", "string"
            )
            nomeCriterio = "Disciplina"
    elif chaveJson == "":
        if criterio == 1:
            valorBusca, _, _, _ = isValidInput(
                "Digite o nome a ser pesquisado: ", "string"
            )
            nomeCriterio = "Nome"
        elif criterio == 2:
            valorBusca, _, _, _ = isValidInput(
                "Digite a matrícula a ser pesquisada: ", "int"
            )
            nomeCriterio = "Matrícula"
        elif criterio == 3:
            valorBusca, _, _, _ = isValidInput(
                "Digite o e-mail a ser pesquisado: ", "string"
            )
            nomeCriterio = "E-mail"

    # Cria uma instância de JsonHandler
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acodor com o retorno do chaveJson
    dados = json_handler.read()
    # get(): Pega valores da chave 'Alunos' no dicionário, caso não exista a chave, retorna vazio
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])
    alunos_professores = alunos + professores
    resultados = []

    # Percorre todo o Json acumulando (qnd mais de 1 resultado) os dados completos daquele aluno
    if chaveJson == "Alunos":
        for aluno in alunos:
            if criterio == 1 and valorBusca.lower() in aluno["nome"].lower():
                resultados.append(aluno)
            elif criterio == 2 and valorBusca == aluno["matricula"]:
                resultados.append(aluno)
            elif criterio == 3 and valorBusca.lower() in aluno["email"].lower():
                resultados.append(aluno)
            elif criterio == 4 and valorBusca.lower() in aluno["curso"].lower():
                resultados.append(aluno)
    elif chaveJson == "Professor":
        for professor in professores:
            if criterio == 1 and valorBusca.lower() in professor["nome"].lower():
                resultados.append(professor)
            elif criterio == 2 and valorBusca == professor["matricula"]:
                resultados.append(professor)
            elif criterio == 3 and valorBusca.lower() in professor["email"].lower():
                resultados.append(professor)
            elif (
                criterio == 4 and valorBusca.lower() in professor["disciplinas"].lower()
            ):
                resultados.append(professor)
    elif chaveJson == "":
        for dado in alunos_professores:
            if criterio == 1 and valorBusca.lower() in dado["nome"].lower():
                resultados.append(dado)
            elif criterio == 2 and valorBusca == dado["matricula"]:
                resultados.append(dado)
            elif criterio == 3 and valorBusca.lower() in dado["email"].lower():
                resultados.append(dado)

    # Se não retornar vazio, mostra os alunos cujo critério deu certo
    if resultados and chaveJson == "Alunos":
        print(
            f"\n{len(resultados)} aluno(s) encontrado(s) com {nomeCriterio} '{valorBusca}':"
        )
        for aluno in resultados:

            mediaNotas = Aluno.calcular_media(aluno["notas"])

            print(f"\nMatrícula: {aluno['matricula']}")
            print(f'Nome: {aluno["nome"]}')
            print(f'Curso: {aluno["curso"]}')
            print(f'Notas: {", ".join(map(str, aluno["notas"]))}')
            print(f"Média das notas: {mediaNotas:.1f}")
            print(f'Presenças: {aluno["presencas"]}')
            print(f'Telefone: {aluno["telefone"]}')
            print(f'Email: {aluno["email"]}')
            print("-" * 30)
    else:
        print(f"\nNenhum aluno encontrado com {nomeCriterio} '{valorBusca}'.")


## Função excluir aluno (dentro do Listar Alunos):
def excluir():
    print("Revisar função excluir...")
    # (
    #     idAlunoExcluir,
    #     erroTipoIdAlunoExcluir,
    #     erroVazioIdAlunoExcluir,
    #     erroMsgIdAlunoExcluir,
    # ) = isValidInput("Digite a matrícula do aluno a ser excluido: ", "int")
    # deleteAluno(idAlunoExcluir, "alunos.json")


## Função alterar aluno (dentro do Listar Alunos):
def alterar(chaveJson):
    # Carrega Json - Alunos e Professores
    dados = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson).read()
    # Só retorna dados se a chaveJson for "Alunos"
    alunos = dados.get("Alunos", [])
    # Só retorna dados se a chaveJson for "Professores"
    professores = dados.get("Professores", [])

    # Alterar Aluno
    if chaveJson == "Alunos":
        (
            matriculaAlunoAlterar,
            _,
            _,
            _,
        ) = isValidInput("Digite a matrícula do aluno a ser alterado: ", "int")

        # Flag
        achoAluno = False
        for aluno in alunos:
            if aluno["matricula"] == matriculaAlunoAlterar:
                achoAluno = True

                # Faz uma cópia profunda do dicionário do aluno
                # Diferente do shallow copy, o que faz com que o objeto interno seja copiado também,
                # evitando assim a referência do objeto original
                alunoAlt = deepcopy(aluno)
                print(f"alunoAlt: {alunoAlt}")
                teste = input("Pressione Enter para continuar...")

                mediaNotas = Aluno.calcular_media(aluno["notas"])

                # Mostra os dados atuais do aluno encontrado:
                print("\n############# Dados Atuais do Aluno #############")
                print(f"\nMatrícula: {aluno['matricula']}")
                print(f'Nome: {aluno["nome"]}')
                print(f'Curso: {aluno["curso"]}')
                print(f'Notas: {", ".join(map(str, aluno["notas"]))}')
                print(f"Média das notas: {mediaNotas:.1f}")
                print(f'Presenças: {aluno["presencas"]}')
                print(f'Telefone: {aluno["telefone"]}')
                print(f'Email: {aluno["email"]}')
                print("-" * 30)
                break
        if not achoAluno:
            print("\n\nAluno não encontrado.\n\n")
            # Retorna e não faz a atualização - Early return pattern
            return

        # Pega os novos dados do aluno (menos a matrícula que não mudam em relação ao aluno)
        novosDados = obterNovosDados(chaveJson, alunoAlt)

        # Salva os dados altualizados no Json
        # Cria instância do objeto de Aluno:
        alunoObj = Aluno(
            matricula=novosDados["matricula"],  # Nesse caso tem que enviar a matrícula
            nome=novosDados["nome"],
            curso=novosDados["curso"],
            notas=novosDados["notas"],  # Já está no formato correto
            presencas=novosDados["presencas"],
            telefone=novosDados["telefone"],
            email=novosDados["email"],
        )
        # A classe JsonHandler é instanciada dentro da classe Alunos
        alunoObj.atualizar()

    # Falta fazer para professor
    elif chaveJson == "Professores":
        # (
        #     matriculaProfessorAlterar,
        #     _,
        #     _,
        #     _,
        # ) = isValidInput("Digite a matrícula do professor a ser alterado: ", "int")

        # # Flag
        # achoProfessor = False
        # for professor in professores:
        #     if professor["matricula"] == matriculaProfessorAlterar:
        #         achoProfessor = True

        #         # Mostra os dados atuais do professor encontrado:
        #         print("\n############# Dados Atuais do professor #############")
        #         print(f"\nMatrícula: {professor['matricula']}")
        #         print(f'Nome: {professor["nome"]}')
        #         print(f'Disciplinas: {professor["disciplinas"]}')
        #         print(f'Turmas: {professor["turmas"]}')
        #         print(f'Telefone: {professor["telefone"]}')
        #         print(f'Email: {professor["email"]}')
        #         print("-" * 30)
        #         break
        # if not achoProfessor:
        #     print("\n\Professor não encontrado.\n\n")
        #     # Retorna e não faz a atualização - Early return pattern
        return

    # Pega os novos dados do professor (menos a matrícula que não mudam em relação ao professor)
    # novosDados = obterNovosDados(chaveJson, professorAlt)
    # updateAluno(matriculaAlunoAlterar, novosDados, "alunos.json")


## Função para "pegar" os novos dados do aluno a ser atualizado
def obterNovosDados(chaveJson, oldData=None):
    if chaveJson == "Alunos":
        novosDados = {}

        # Poderia pegar dentro da função alterar, mas fazendo aqui fica mais organizado
        novosDados["matricula"] = oldData["matricula"]

        print(f'Nome atual: {oldData["nome"]}')
        novosDados["nome"], _, _, _ = isValidInput(
            "Digite o novo nome do aluno ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["nome"] == "":
            novosDados["nome"] = oldData["nome"]

        print(f'\nCurso atual: {oldData["curso"]}')
        novosDados["curso"], _, _, _ = isValidInput(
            "Digite o novo curso do aluno ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["curso"] == "":
            novosDados["curso"] = oldData["curso"]

        print(f'\nPresenças atual: {oldData["presencas"]}')
        (
            novosDados["presencas"],
            _,
            _,
            _,
        ) = isValidInput(
            "Digite o novo número de presenças do aluno ou Enter para manter o atual: ",
            "int",
            aceitaVazio=True,
        )
        if novosDados["presencas"] == "":
            novosDados["presencas"] = int(oldData["presencas"])

        print(f'\nTelefone atual: {oldData["telefone"]}')
        (
            novosDados["telefone"],
            _,
            _,
            _,
        ) = isValidInput(
            "Digite o novo telefone do aluno ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["telefone"] == "":
            novosDados["telefone"] = oldData["telefone"]

        print(f'\nEmail atual: {oldData["email"]}')
        novosDados["email"], _, _, _ = isValidInput(
            "Digite o novo email do aluno ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["email"] == "":
            novosDados["email"] = oldData["email"]

        # Entrada das notas do aluno:
        print(f'\nNotas atuais: {", ".join(map(str, oldData["notas"]))}')
        # Na verdade só verifica se está vazio ou não: vazio mantém as notas antigas, != vazio chama a função trataNotasAluno
        novosDados["notas"], _, _, _ = isValidInput(
            "Digite '1' para alterar as notas do aluno ou Enter para manter a(s) nota(s): ",
            "string",
            aceitaVazio=True,
        )
        novosDados["notas"] = (
            trataNotasAluno() if novosDados["notas"] != "" else oldData["notas"]
        )

        return novosDados


## Função exibir tela de cadastro novo aluno:
def telaCadastro():
    print("Revisar função telaCadastro...")


#     print("\n\n############# Cadastro de Aluno #############")

#     # Preparação dados:
#     novoAluno = {}

#     novoAluno["matricula"] = (
#         None  # Inicializando a matrícula, que será incrementada e inserida automaticamente ao cadastro do aluno
#     )
#     novoAluno["nome"], erroTipoNomeAluno, erroVazioNomeAluno, erroMsgNomeAluno = (
#         isValidInput("Digite o nome do aluno: ", "string")
#     )
#     novoAluno["curso"], erroTipoCursoAluno, erroVazioCursoAluno, erroMsgCursoAluno = (
#         isValidInput("Digite o curso: ", "string")
#     )
#     novoAluno["presencas"], erroTipoPresencas, erroVazioPresencas, erroMsgPresencas = (
#         isValidInput("Digite o número de presenças: ", "int")
#     )
#     novoAluno["telefone"], erroTipoTelefone, erroVazioTelefone, erroMsgTelefone = (
#         isValidInput("Digite o telefone: ", "string")
#     )
#     novoAluno["email"], erroTipoEmail, erroVazioEmail, erroMsgEmail = isValidInput(
#         "Digite o email: ", "string"
#     )
#     # Entrada das notas do aluno:
#     novoAluno["notas"] = trataNotasAluno()  # Exemplo de retorno: [9.5, 6.5, 8.2]

#     # Create no Json
#     try:
#         createAluno(novoAluno, "alunos.json")
#         print(
#             "\n\n########################### Aluno cadastrado com sucesso! ###########################\n"
#         )
#     except Exception as e:
#         print(f"Erro ao criar o aluno: {e}")


# ## Função utilizada tratar notas no momento do cadastro do aluno:
def trataNotasAluno():

    numNotas, _, _, _ = isValidInput(
        "Informe o número de notas a serem cadastradas: ", "int"
    )
    notas = []
    for i in range(numNotas):
        while True:
            nota, _, _, _ = isValidInput(f"Informe a {i+1}ª nota: ", "float")
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
def isValidInput(msg, tipoEsperado, aceitaVazio=False):

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
        # Verifica se está vazio e se deveria estar: Não aceita mas está?  Erro
        if (aceitaVazio == False) and (len(valor) == 0):
            erroMsg = "Entrada vazia não é permitida."
            print(erroMsg)
            valor = input(msg)
        # Verifica se está vazio e se deveria estar: Aceita vazio e está vazio? Tudo certo!
        # Não verifica mais nada!
        elif (aceitaVazio == True) and (len(valor) == 0):
            erroTipo = False
            erroVazio = False
            break
        else:
            # Se o tipo esperado for string, todos os valores são aceitos
            if tipoEsperado == "string":
                erroTipo = False
                break
            elif tipoEsperado == "int":
                try:
                    valor = int(valor)
                    erroTipo = False
                    break
                except ValueError:
                    erroTipo = True
                    erroMsg = "Entrada inválida. O valor deve ser um inteiro."
                    print(erroMsg)
                    valor = input(msg)
            elif tipoEsperado == "float":
                try:
                    valor = float(valor)
                    erroTipo = False
                    break
                except ValueError:
                    erroTipo = True
                    erroMsg = "Entrada inválida. O valor deve ser um float."
                    print(erroMsg)
                    valor = input(msg)
            elif tipoEsperado == "intFloat":
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

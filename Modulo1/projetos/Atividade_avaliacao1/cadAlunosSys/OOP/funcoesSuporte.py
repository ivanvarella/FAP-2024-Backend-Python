import os
from aluno import Aluno
from professor import Professor
from jsonHandler import JsonHandler
from copy import (
    deepcopy,
)  # Cópia profunda dos dados de alunos / professores sem risco de "comtaminação"
import platform  # Para abrir o navegador padrão

# Teste Menu com Rich
import rich_menus as richs

# Gerar o arquivo PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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


# ## Função exibir menu opções:
def exibirMenuPrincipal(tipo="default"):
    if tipo == "default":
        print("\n\n############ Menu Principal #############")
        print("#              [ Alunos ]               #")
        print("#                                       #")
        print("#   Cod[1]: Cadastrar Aluno             #")
        print("#   Cod[2]: Listar / Alterar / excluir  #")
        print("#   Cod[3]: Pesquisar Aluno             #")
        print("# ------------------------------------- #")
        print("#          [ Professores ]              #")
        print("#                                       #")
        print("#   Cod[4]: Cadastrar Professor         #")
        print("#   Cod[5]: Listar / Alterar / Excluir  #")
        print("#   Cod[6]: Pesquisar Professor         #")
        print("# ------------------------------------- #")
        print("#          [ Outras opções ]            #")
        print("#                                       #")
        print("#   Cod[7]:  Listar                     #")
        print("#   Cod[8]:  Pesquisar                  #")
        print("#   Cod[9]:  Dados no navegador         #")
        print("#   Cod[10]: Gerar PDF com os dados     #")
        print("# ------------------------------------- #")
        print("#                                       #")
        print("#   Cod[11]: Sair                       #")
        print("#   Cod[0]: Sobre                       #")
        print("#                                       #")
        print("#########################################\n")
    elif tipo == "rich1":
        richs.principal_rich1()
    elif tipo == "rich2":
        richs.principal_rich2()

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
        ) = isValidInput("Digite Enter para voltar. ", "string", aceitaVazio=True)
        return


## Função Sair:
def sair():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("#########################################################")
    print("#  Obrigado por usar o Sistema de Cadastro de Alunos    #")
    print("#########################################################")
    print("\n\n\n\n\n")


## Exibir Menu Pesquisar
def exibirMenuPesquisarCriterio(chaveJson):
    if chaveJson == "Alunos":
        print("\n\n#######  Menu Pesquisar  #######")
        print("#                              #")
        print("#         [Alunos]             #")
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
        print("#       [Professores]          #")
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
        print("\n\nNenhum dado cadastrado.\n\n")
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

    while True:
        # Opção alterar ou excluir aluno ou professor dentro de listar, para facilitar,
        # já que o usuário poderá visualizar os alunos antes de realizar as alterações:
        opcaoMenuAlterarExcluir = exibirMenuAlterarExcluir(chaveJson)
        # Controla os opções do Menu Alterar / Excluir aluno
        if opcaoMenuAlterarExcluir == 3:
            return  # Volta para o o loop do menu principal
        elif opcaoMenuAlterarExcluir == 1:
            alterar(chaveJson)
            break
        elif opcaoMenuAlterarExcluir == 2:
            excluir(chaveJson)
            break
        elif opcaoMenuAlterarExcluir == None:
            return
        else:
            print("\nOpção inválida!\n")


## Função pesquisar
def pesquisar(chaveJson=""):

    # Exibir menu principal da pesquisa + obter o critério da pesquisa
    criterio = exibirMenuPesquisarCriterio(chaveJson)

    # Obtém o valor a ser pesquisado
    # Pesquisa de dados de Alunos
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
    # Pesquisa de dados de Professores
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
    # Pesquisa de dados quaisquer - chaveJson = ""
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

    # Cria uma instância de JsonHandler - Alunos ou Professores -> chavePrincipal
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acodor com o retorno do chaveJson
    dados = json_handler.read()
    # get(): Pega valores da chave 'Alunos' ou 'Professores' no Json, caso não exista a chave, retorna vazio
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])
    # Quando chaveJson = ""
    resultados = []
    resultados_alunos = []
    resultados_professores = []

    # Percorre todos os dados filtrados do Json
    # Somente Alunos
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
    # Somente Professores
    elif chaveJson == "Professores":
        for professor in professores:
            if criterio == 1 and valorBusca.lower() in professor["nome"].lower():
                resultados.append(professor)
            elif criterio == 2 and valorBusca == professor["matricula"]:
                resultados.append(professor)
            elif criterio == 3 and valorBusca.lower() in professor["email"].lower():
                resultados.append(professor)
            # Função geradora any() + for = percorre cada posição da lista disciplina,
            # executando o lower() e comparando
            elif criterio == 4 and any(
                valorBusca.lower() in disciplina.lower()
                for disciplina in professor["disciplinas"]
            ):
                resultados.append(professor)
    # Alunos ou Professores
    elif chaveJson == "":
        # Pega todos os alunos
        for dado in alunos:
            if criterio == 1 and valorBusca.lower() in dado["nome"].lower():
                resultados_alunos.append(dado)
            elif criterio == 2 and valorBusca == dado["matricula"]:
                resultados.append(dado)
            elif criterio == 3 and valorBusca.lower() in dado["email"].lower():
                resultados.append(dado)
        # Pega todos os professores
        for professor in professores:
            if criterio == 1 and valorBusca.lower() in professor["nome"].lower():
                resultados_professores.append(professor)
            elif criterio == 2 and valorBusca == professor["matricula"]:
                resultados_professores.append(professor)
            elif criterio == 3 and valorBusca.lower() in professor["email"].lower():
                resultados_professores.append(professor)

    # Se não retornar vazio, mostra os alunos cujo critério deu certo
    if resultados and chaveJson == "Alunos":
        print("-" * 60)
        print(
            f"\n ###   {len(resultados)} aluno(s) encontrado(s) com {nomeCriterio} '{valorBusca}'   ###"
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
    elif resultados and chaveJson == "Professores":
        print("-" * 60)
        print(
            f"\n ###   {len(resultados)} professor(es) encontrado(s) com {nomeCriterio} '{valorBusca}'   ###"
        )
        for professor in resultados:

            print(f"\nMatrícula: {professor['matricula']}")
            print(f'Nome: {professor["nome"]}')
            print(f'Disciplinas: {professor["disciplinas"]}')
            print(f'Turmas: {professor["turmas"]}')
            print(f'Telefone: {professor["telefone"]}')
            print(f'Email: {professor["email"]}')
            print("-" * 30)
    elif (resultados_alunos or resultados_professores) and chaveJson == "":
        print("-" * 60)
        print(
            f"\n ###   {len(resultados_alunos + resultados_professores)} dado(s) encontrado(s) com {nomeCriterio} '{valorBusca}'   ###"
            f"\n ### {len(resultados_alunos)} Aluno(s) e {len(resultados_professores)} Professor(es) ###"
        )
        if resultados_alunos:
            print("\n\n############# Lista de Alunos #############")
            for aluno in resultados_alunos:

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
        if resultados_professores:
            print("\n\n############# Lista de Professores #############")
            for professor in resultados_professores:

                print(f"\nMatrícula: {professor['matricula']}")
                print(f'Nome: {professor["nome"]}')
                print(f'Disciplinas: {professor["disciplinas"]}')
                print(f'Turmas: {professor["turmas"]}')
                print(f'Telefone: {professor["telefone"]}')
                print(f'Email: {professor["email"]}')
                print("-" * 30)
    # Se não encontrou nenhum dado entre todos
    else:
        print(f"\nNenhum dado encontrado com {nomeCriterio} '{valorBusca}'.")
    input("Pressione Enter para continuar...\n")


## Função excluir aluno (dentro do Listar Alunos):
def excluir(chaveJson):

    (
        matriculaExcluir,
        _,
        _,
        _,
    ) = isValidInput("Digite a matrícula da entidade a ser excluida: ", "int")
    # Exclui pela matrícula - Aluno ou Professor
    JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson).delete(
        matriculaExcluir
    )


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

    # Alterar Professores
    elif chaveJson == "Professores":
        (
            matriculaProfessorAlterar,
            _,
            _,
            _,
        ) = isValidInput("Digite a matrícula do professor a ser alterado: ", "int")

        # Flag
        achoProfessor = False
        for professor in professores:
            if professor["matricula"] == matriculaProfessorAlterar:
                achoProfessor = True

                # Faz uma cópia profunda do dicionário do professor
                # Diferente do shallow copy, o que faz com que o objeto interno seja copiado também,
                # evitando assim a referência do objeto original
                professorAlt = deepcopy(professor)

                # Mostra os dados atuais do professor encontrado:
                print("\n############# Dados Atuais do Professor #############")
                print(f"\nMatrícula: {professor['matricula']}")
                print(f'Nome: {professor["nome"]}')
                print(f'Disciplinas: {professor["disciplinas"]}')
                print(f'Turmas: {professor["turmas"]}')
                print(f'Telefone: {professor["telefone"]}')
                print(f'Email: {professor["email"]}')
                print("-" * 30)
                break
        if not achoProfessor:
            print("\n\nProfessor não encontrado.\n\n")
            # Retorna e não faz a atualização - Early return pattern
            return

        # Pega os novos dados do professor (menos a matrícula que não mudam em relação ao professor)
        # Passa os dados antigos para mostrar como referência para alteração
        novosDados = obterNovosDados(chaveJson, professorAlt)

        # Salva os dados altualizados no Json
        # Cria instância do objeto de Aluno:
        professorObj = Professor(
            matricula=novosDados[
                "matricula"
            ],  # Nesse caso tem que enviar a matrícula - update
            nome=novosDados["nome"],
            disciplinas=novosDados["disciplinas"],
            turmas=novosDados["turmas"],
            telefone=novosDados["telefone"],
            email=novosDados["email"],
        )
        # A classe JsonHandler é instanciada dentro da classe Alunos
        professorObj.atualizar()


## Função para "pegar" os novos dados do aluno a ser atualizado
def obterNovosDados(chaveJson, oldData=None):
    # Para Alunos
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

    # Para Professores
    elif chaveJson == "Professores":
        novosDados = {}

        # Poderia pegar dentro da função alterar, mas fazendo aqui fica mais organizado
        novosDados["matricula"] = oldData["matricula"]

        print(f'Nome atual: {oldData["nome"]}')
        novosDados["nome"], _, _, _ = isValidInput(
            "Digite o novo nome do professor ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["nome"] == "":
            novosDados["nome"] = oldData["nome"]

        print(f'\nDisciplinas atuais: {oldData["disciplinas"]}')
        novosDados["disciplinas"], _, _, _ = isValidInput(
            "Digite 1 para alterar as disciplinas ou Enter para manter as atuais: ",
            "string",
            aceitaVazio=True,
        )
        novosDados["disciplinas"] = (
            trataDisciplinasTurmas("disciplinas")
            if novosDados["disciplinas"] != ""
            else oldData["disciplinas"]
        )

        print(f'\nTurmas atuais: {oldData["turmas"]}')
        novosDados["turmas"], _, _, _ = isValidInput(
            "Digite 1 para alterar as turmas ou Enter para manter as atuais: ",
            "string",
            aceitaVazio=True,
        )
        novosDados["turmas"] = (
            trataDisciplinasTurmas("turmas")
            if novosDados["turmas"] != ""
            else oldData["turmas"]
        )

        print(f'\nTelefone atual: {oldData["telefone"]}')
        (
            novosDados["telefone"],
            _,
            _,
            _,
        ) = isValidInput(
            "Digite o novo telefone do professor ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["telefone"] == "":
            novosDados["telefone"] = oldData["telefone"]

        print(f'\nEmail atual: {oldData["email"]}')
        novosDados["email"], _, _, _ = isValidInput(
            "Digite o novo email do professor ou Enter para manter o atual: ",
            "string",
            aceitaVazio=True,
        )
        if novosDados["email"] == "":
            novosDados["email"] = oldData["email"]

        return novosDados


## Função exibir tela de cadastro novo aluno:
def telaCadastro(chaveJson):

    if chaveJson == "Alunos":
        print("\n\n############# Cadastro de Aluno #############")
        # Preparação dados:
        novoAluno = {}

        novoAluno["matricula"] = (
            None  # Inicializando a matrícula, que será incrementada e inserida automaticamente ao cadastro do aluno
        )
        novoAluno["nome"], _, _, _ = isValidInput("Digite o nome do aluno: ", "string")
        novoAluno["curso"], _, _, _ = isValidInput("Digite o curso: ", "string")
        novoAluno["presencas"], _, _, _ = isValidInput(
            "Digite o número de presenças: ", "int"
        )
        novoAluno["telefone"], _, _, _ = isValidInput("Digite o telefone: ", "string")
        novoAluno["email"], _, _, _ = isValidInput("Digite o email: ", "string")
        # Entrada das notas do aluno:
        novoAluno["notas"] = trataNotasAluno()  # Exemplo de retorno: [9.5, 6.5, 8.2]

        # Salva os dados altualizados no Json
        # Cria instância do objeto de Aluno:
        alunoObj = Aluno(
            matricula=None,  # Criado dentro do JsonHandler, passando aqui para ficar organizado no arquivo Json
            nome=novoAluno["nome"],
            curso=novoAluno["curso"],
            notas=novoAluno["notas"],  # Já está no formato correto
            presencas=novoAluno["presencas"],
            telefone=novoAluno["telefone"],
            email=novoAluno["email"],
        )
        # A classe JsonHandler é instanciada dentro da classe Alunos
        alunoObj.salvar()

    if chaveJson == "Professores":
        print("\n\n############# Cadastro de Professor #############")
        # Preparação dados:
        novoProfessor = {}

        novoProfessor["matricula"] = (
            None  # Inicializando a matrícula, que será incrementada e inserida automaticamente ao cadastro do aluno
        )
        novoProfessor["nome"], _, _, _ = isValidInput(
            "Digite o nome do professor: ", "string"
        )
        novoProfessor["telefone"], _, _, _ = isValidInput(
            "Digite o telefone: ", "string"
        )
        novoProfessor["email"], _, _, _ = isValidInput("Digite o email: ", "string")

        # Entrada das disciplinas e turmas do Professor:
        novoProfessor["disciplinas"] = trataDisciplinasTurmas(
            "disciplinas"
        )  # Exemplo de retorno: ["Matemática", "Física", "Programação"]
        novoProfessor["turmas"] = trataDisciplinasTurmas(
            "turmas"
        )  # Exemplo de retorno: ["Eng.Comp_2024.2", "Física_2023.1", "Matemática_2022.2"]

        # Salva os dados altualizados no Json
        # Cria instância do objeto de Professor:
        professorObj = Professor(
            matricula=None,  # Criado dentro do JsonHandler, passando aqui para ficar organizado no arquivo Json
            nome=novoProfessor["nome"],
            disciplinas=novoProfessor["disciplinas"],
            turmas=novoProfessor["turmas"],
            telefone=novoProfessor["telefone"],
            email=novoProfessor["email"],
        )
        # A classe JsonHandler é instanciada dentro da classe Alunos
        professorObj.salvar()


# ## Função para tratar disciplinas e turmas do professor
def trataDisciplinasTurmas(tipo):
    """
    Função para capturar uma lista de disciplinas ou turmas do usuário.

    Args:
        tipo (str): Tipo de dado a ser capturado (por exemplo, 'disciplina' ou 'turma').

    Returns:
        list: Lista de disciplinas ou turmas inseridas pelo usuário.
    """
    dados = []
    while True:
        # Solicita a entrada do usuário e permite entrada vazia para finalizar
        entradaDado, _, _, _ = isValidInput(
            f"\nDigite a {tipo[:-1]} a ser cadastrada ou Enter para finalizar o cadastro das {tipo}: ",
            "string",
            aceitaVazio=True,
        )

        # Verifica se a entrada é vazia para sair do loop e retornar os dados
        if entradaDado.lower() == "":
            break

        # Adiciona a entrada à lista de dados
        dados.append(entradaDado)

        # Converte a lista de dados em uma string para exibição
        dados_str = ", ".join(dados)

        # Exibe a lista atual de entradas
        print(f"\n{tipo.capitalize()} já foram inseridas: {dados_str}.\n")
    return dados


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
# - aceitaVazio: padrão False (não aceitando valors vazios), caso aceite, declarar True - Não faz nenhuma verificação
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


# Popula o arquivo html com os dados do Json
# chaveJson não está sendo utilizado no momento, mas pode ser usada para filtrar os
# dados no futuro, dependendo da necessidade.
def gera_html(arquivo_html, chaveJson):
    # Cria uma instância de JsonHandler
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acordo com o retorno do chaveJson
    dados = json_handler.read()
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])

    # Se tiver buscado por Alunos e não existir nenhum
    if chaveJson == "Alunos" and not alunos:
        print("\n\nNenhum Aluno cadastrado.\n\n")
        return

    # Se tiver buscado por Professores e não existir nenhum
    if chaveJson == "Professores" and not professores:
        print("\n\nNenhum Professor cadastrado.\n\n")
        return

    # Se tiver buscado por Dados e não existir nenhum
    if chaveJson == "" and not (alunos or professores):
        print("\n\nNenhum dado cadastrado.\n\n")
        return

    # Criando o arquivo HTML
    with open(arquivo_html, "w", encoding="utf-8") as html_file:
        html_file.write(
            """
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
            <meta charset="utf-8">
            <title>Relatório de Dados</title>
            <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
            header { background-color: #4CAF50; color: white; padding: 10px 0; text-align: center; }
            .container { width: 80%; margin: auto; padding: 20px; }
            .button { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; margin: 10px; cursor: pointer; border-radius: 5px; }
            .button:hover { background-color: #45a049; }
            .section { display: none; margin-bottom: 20px; padding: 20px; border-radius: 5px; background-color: #f4f4f4; }
            .section.active { display: block; }
            .section h2 { color: #333; }
            .item { margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: white; }
            .item p { margin: 5px 0; }
            .item hr { margin: 10px 0; }
            </style>
            <script>
            function showSection(sectionId) {
                var sections = document.querySelectorAll('.section');
                sections.forEach(function(section) {
                    section.classList.remove('active');
                });
                var section = document.getElementById(sectionId);
                if (section) {
                    section.classList.add('active');
                } else {
                    console.warn('Elemento com ID "' + sectionId + '" não encontrado.');
                }
            }
            window.onload = function() {
                var defaultSection = document.querySelector('.button').getAttribute('data-target');
                if (defaultSection) {
                    showSection(defaultSection);
                }
            }
            </script>
            </head>
            <body>
            <header>
                <h1>Relatório de Dados</h1>
            </header>
            <div class="container">
                <button class="button" data-target="alunosSection" onclick="showSection('alunosSection')">Mostrar Alunos</button>
                <button class="button" data-target="professoresSection" onclick="showSection('professoresSection')">Mostrar Professores</button>
                <button class="button" data-target="allSection" onclick="showSection('allSection')">Mostrar Todos</button>
        """
        )

        # Para alunos
        if alunos:
            html_file.write(
                """
                <div id="alunosSection" class="section">
                    <h2>Lista de Alunos</h2>
                    <p>Total de alunos cadastrados: {}</p>
                """.format(
                    len(alunos)
                )
            )

            for aluno in alunos:
                media_notas = Aluno.calcular_media(aluno["notas"])
                html_file.write(
                    """
                    <div class="item">
                        <p><strong>Matrícula:</strong> {}</p>
                        <p><strong>Nome:</strong> {}</p>
                        <p><strong>Curso:</strong> {}</p>
                        <p><strong>Notas:</strong> {}</p>
                        <p><strong>Média das notas:</strong> {:.1f}</p>
                        <p><strong>Presenças:</strong> {}</p>
                        <p><strong>Telefone:</strong> {}</p>
                        <p><strong>Email:</strong> {}</p>
                    </div>
                    """.format(
                        aluno["matricula"],
                        aluno["nome"],
                        aluno["curso"],
                        ", ".join(map(str, aluno["notas"])),
                        media_notas,
                        aluno["presencas"],
                        aluno["telefone"],
                        aluno["email"],
                    )
                )
            html_file.write("</div>")
        else:
            html_file.write(
                """
                <div id="alunosSection" class="section">
                    <h2>Nenhum aluno cadastrado</h2>
                </div>
                """
            )

        # Para professores
        if professores:
            html_file.write(
                """
                <div id="professoresSection" class="section">
                    <h2>Lista de Professores</h2>
                    <p>Total de Professores cadastrados: {}</p>
                """.format(
                    len(professores)
                )
            )

            for professor in professores:
                html_file.write(
                    """
                    <div class="item">
                        <p><strong>Matrícula:</strong> {}</p>
                        <p><strong>Nome:</strong> {}</p>
                        <p><strong>Disciplinas:</strong> {}</p>
                        <p><strong>Turmas:</strong> {}</p>
                        <p><strong>Telefone:</strong> {}</p>
                        <p><strong>Email:</strong> {}</p>
                    </div>
                    """.format(
                        professor["matricula"],
                        professor["nome"],
                        professor["disciplinas"],
                        professor["turmas"],
                        professor["telefone"],
                        professor["email"],
                    )
                )
            html_file.write("</div>")
        else:
            html_file.write(
                """
                <div id="professoresSection" class="section">
                    <h2>Nenhum professor cadastrado</h2>
                </div>
                """
            )

        # Para todos os dados
        if alunos or professores:
            html_file.write(
                """
                <div id="allSection" class="section">
                """
            )
            # Só cria os dados de Alunos se existir
            if alunos:
                html_file.write(
                    """
                    <h2>Lista de Alunos</h2>
                    <p>Total de alunos cadastrados: {}</p>
                """.format(
                        len(alunos)
                    )
                )
                for aluno in alunos:
                    media_notas = Aluno.calcular_media(aluno["notas"])
                    html_file.write(
                        """
                        <div class="item">
                            <p><strong>Matrícula:</strong> {}</p>
                            <p><strong>Nome:</strong> {}</p>
                            <p><strong>Curso:</strong> {}</p>
                            <p><strong>Notas:</strong> {}</p>
                            <p><strong>Média das notas:</strong> {:.1f}</p>
                            <p><strong>Presenças:</strong> {}</p>
                            <p><strong>Telefone:</strong> {}</p>
                            <p><strong>Email:</strong> {}</p>
                        </div>
                        """.format(
                            aluno["matricula"],
                            aluno["nome"],
                            aluno["curso"],
                            ", ".join(map(str, aluno["notas"])),
                            media_notas,
                            aluno["presencas"],
                            aluno["telefone"],
                            aluno["email"],
                        )
                    )
            # Só cria os dados de Professores se existir
            if professores:
                html_file.write(
                    """
                    <h2>Lista de Professores</h2>
                    <p>Total de Professores cadastrados: {}</p>
                    """.format(
                        len(professores)
                    )
                )
                for professor in professores:
                    html_file.write(
                        """
                        <div class="item">
                            <p><strong>Matrícula:</strong> {}</p>
                            <p><strong>Nome:</strong> {}</p>
                            <p><strong>Disciplinas:</strong> {}</p>
                            <p><strong>Turmas:</strong> {}</p>
                            <p><strong>Telefone:</strong> {}</p>
                            <p><strong>Email:</strong> {}</p>
                        </div>
                        """.format(
                            professor["matricula"],
                            professor["nome"],
                            professor["disciplinas"],
                            professor["turmas"],
                            professor["telefone"],
                            professor["email"],
                        )
                    )
                html_file.write("</div>")
        else:
            html_file.write(
                """
                <div id="allSection" class="section">
                    <h2>Nenhum dado cadastrado</h2>
                </div>
                """
            )

        html_file.write("</div></body></html>")


def verifica_arquivo(arquivo, tipo):
    global caminho

    # Para arquivo html
    if tipo == "html":
        # Verifica se o arquivo HTML já existe
        if os.path.isfile(arquivo):
            # Se o arquivo existe, abre em modo de escrita para limpar seu conteúdo
            with open(arquivo, "w", encoding="utf-8") as file:
                # pass dentro do contexto with open() no modo escrita (w),
                # o arquivo será limpo, ou truncado.
                pass  # Não escreve nada, apenas limpa o conteúdo
        else:
            # Se o arquivo não existe, ele será criado
            with open(arquivo, "w", encoding="utf-8") as file:
                pass  # Cria um arquivo vazio

    # Para arquivo pdf
    elif tipo == "pdf":
        # Verifica se o arquivo já existe
        if os.path.exists(arquivo):
            print(f"Arquivo {arquivo} já existe.")
            while True:
                novo_pdf = input(
                    "Digite Enter para sobrescrevê-lo ou digite o nome do novo arquivo a ser criado: "
                ).strip()

                # Se o usuário digitar um novo nome, verifica se é válido e se não é o mesmo nome
                if novo_pdf:
                    # Adiciona a extensão .pdf se não estiver presente
                    if not novo_pdf.lower().endswith(".pdf"):
                        novo_pdf += ".pdf"
                    novo_arquivo_pdf_completo = os.path.join(caminho, novo_pdf)
                    if novo_arquivo_pdf_completo != arquivo:
                        return novo_arquivo_pdf_completo
                    else:
                        print(
                            "Nome inválido. O nome digitado é o mesmo do arquivo já existente. Tente novamente."
                        )
                else:
                    # Se o usuário não digitar nada, sobrescreve o arquivo existente
                    return arquivo
        else:
            # Se o arquivo não existir, retorna o nome do arquivo original que será sobrescrito
            return arquivo


# Abre um link ou o arquivo html no navegador padrão
def abrir_link(file_url):
    if platform.system() == "Windows":
        os.system(f"start {file_url}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {file_url}")
    else:  # Linux
        os.system(f"xdg-open {file_url}")
        # Brs para mover os warnings do xdg-open
        # Enquanto o navegador estiver aberto o terminal ficará "travado" com a instância do xdg-open
        # só será efetivo quando fechar
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# arquivo_html = nome do arquivo e extesão (exemplo: "dados.html")
# chaveJson (opcional, "" por padrão): No contexto desse programa: "Alunos" ou "Professores"
# Usado para saber quais dados serão gerados: chaveJson = "", é para retornar todos os dados\
def html(arquivo_html, chaveJson=""):

    # Caminho completo do arquivo HTML
    global caminho
    arquivo_html = os.path.join(caminho, arquivo_html)

    # Verifica se o arquivo existe, se existir limpa, se não cria
    verifica_arquivo(arquivo_html, "html")

    # Se o arquivo não existir, será criado
    gera_html(arquivo_html, chaveJson)

    # Tem que ter o "https://" ou o "http://"
    # file_url = "https://www.google.com"
    file_url = arquivo_html
    abrir_link(file_url)


# Passando chaveJson para futura espanção do código, não está sendo utilizando no momento
def pdf(arquivo_pdf, chaveJson=""):
    """
    Gera um arquivo PDF com os dados de alunos e professores.

    Args:
    arquivo_pdf (str): Nome do arquivo PDF.
    chaveJson (str): Chave para filtrar os dados do JSON.
    """

    # Caminho completo do arquivo HTML
    global caminho
    arquivo_pdf = os.path.join(caminho, arquivo_pdf)

    # Verifica se o arquivo já existe, caso exista, pergunta se quer substituir ou criar novo
    arquivo_pdf_verificado = verifica_arquivo(arquivo_pdf, "pdf")
    # Se retornar o mesmo, sobrescreve -> Deleta o arquivo existente e cria um novo com mesmo nome
    if arquivo_pdf_verificado == arquivo_pdf:
        # Verifica se existe antes de deletar, caso contrário dá erro
        if os.path.exists(arquivo_pdf):
            os.remove(arquivo_pdf)
    else:
        # Se não, pega o novo nome de arquivo retornado de verifica_arquivo()
        # Já vem com o caminho completo do arquivo
        arquivo_pdf = arquivo_pdf_verificado

    # Cria uma instância de JsonHandler
    json_handler = JsonHandler(arquivoJson="dados.json", chavePrincipal=chaveJson)

    # Pega todos os dados e "filtra" de acordo com o retorno do chaveJson
    dados = json_handler.read()
    alunos = dados.get("Alunos", [])
    professores = dados.get("Professores", [])

    # Se não existir nenhum dado para gerar o PDF, retorna
    if chaveJson == "Alunos" and not alunos:
        print("\n\nNenhum Aluno cadastrado.\n\n")
        return
    elif chaveJson == "Professores" and not professores:
        print("\n\nNenhum Professor cadastrado.\n\n")
        return
    elif chaveJson == "" and not (alunos or professores):
        print("\n\nNenhum dado cadastrado.\n\n")
        return

    # Cria o PDF
    c = canvas.Canvas(arquivo_pdf, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)

    # Adiciona o título
    c.drawString(200, height - 40, "Relatório de Dados")

    y_position = height - 60

    def check_page_full(y_pos):
        """Verifica se a posição Y está no final da página e adiciona uma nova página se necessário."""
        if y_pos < 50:  # Ajuste o limite conforme necessário
            c.showPage()  # Adiciona uma nova página
            c.setFont("Helvetica", 12)
            y_pos = height - 40  # Redefine a posição vertical inicial na nova página
        return y_pos

    # Adiciona dados dos alunos
    if alunos:
        c.drawString(30, y_position, f"Lista de Alunos ({len(alunos)}):")
        y_position -= 20
        for aluno in alunos:
            y_position = check_page_full(y_position)
            media_notas = sum(aluno["notas"]) / len(aluno["notas"])
            c.drawString(30, y_position, f"Matrícula: {aluno['matricula']}")
            y_position -= 20
            c.drawString(30, y_position, f"Nome: {aluno['nome']}")
            y_position -= 20
            c.drawString(30, y_position, f"Curso: {aluno['curso']}")
            y_position -= 20
            c.drawString(
                30, y_position, f"Notas: {', '.join(map(str, aluno['notas']))}"
            )
            y_position -= 20
            c.drawString(30, y_position, f"Média das notas: {media_notas:.1f}")
            y_position -= 20
            c.drawString(30, y_position, f"Presenças: {aluno['presencas']}")
            y_position -= 20
            c.drawString(30, y_position, f"Telefone: {aluno['telefone']}")
            y_position -= 20
            c.drawString(30, y_position, f"Email: {aluno['email']}")
            y_position -= 40

    # Adiciona dados dos professores
    if professores:
        # Desenha uma linha horizontal no meio da página
        c.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        c.setLineWidth(2)  # Largura da linha
        y_position = check_page_full(y_position)
        c.line(30, y_position + 15, width - 30, y_position + 15)  # Linha horizontal
        c.drawString(30, y_position, f"Lista de Professores ({len(professores)}):")
        y_position -= 20
        for professor in professores:
            y_position = check_page_full(y_position)
            c.drawString(30, y_position, f"Matrícula: {professor['matricula']}")
            y_position -= 20
            c.drawString(30, y_position, f"Nome: {professor['nome']}")
            y_position -= 20
            c.drawString(30, y_position, f"Disciplinas: {professor['disciplinas']}")
            y_position -= 20
            c.drawString(30, y_position, f"Turmas: {professor['turmas']}")
            y_position -= 20
            c.drawString(30, y_position, f"Telefone: {professor['telefone']}")
            y_position -= 20
            c.drawString(30, y_position, f"Email: {professor['email']}")
            y_position -= 40

    # Salva o PDF
    c.save()
    print(f"\n\nPDF gerado com sucesso em {arquivo_pdf}\n")
    input("Digite Enter para continuar... \n\n")

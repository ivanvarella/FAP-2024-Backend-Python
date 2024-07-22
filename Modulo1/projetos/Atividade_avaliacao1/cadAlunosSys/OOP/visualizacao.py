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
    opcaoMenuPrincipal, _, _, _ = isValidInput("Digite a opção desejada: ", "int")
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
        criterio, _, _, _ = isValidInput("Digite a opção desejada: ", "int")
        if criterio not in [1, 2, 3, 4, 5]:  # Corrigido de "is not in" para "not in"
            print("Opção inválida.")
        else:
            break
    return criterio

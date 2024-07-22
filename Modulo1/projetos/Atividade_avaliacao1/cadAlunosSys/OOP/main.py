##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####
##### Ricardo Nogueira ####

import funcoesSuporte as func


# Controle Menu Principal:
while True:

    # Exibir menu principal - Pega o retorno do input interno:
    opcaoMenuPrincipal = func.exibirMenuPrincipal()

    if opcaoMenuPrincipal == 1:
        func.telaCadastro("Alunos")
    elif opcaoMenuPrincipal == 2:
        func.listar("Alunos")
    elif opcaoMenuPrincipal == 3:
        func.pesquisar("Alunos")
    elif opcaoMenuPrincipal == 4:
        func.telaCadastro("Professores")
    elif opcaoMenuPrincipal == 5:
        func.listar("Professores")
    elif opcaoMenuPrincipal == 6:
        func.pesquisar("Professores")
    elif opcaoMenuPrincipal == 7:
        func.listar()
    elif opcaoMenuPrincipal == 8:
        func.pesquisar()
    elif opcaoMenuPrincipal == 9:
        func.sair()
        break
    elif opcaoMenuPrincipal == 0:
        func.sobre()
    else:
        print("Opção inválida. Tente novamente.")

    # print("\n\n########### Menu Principal ############")
    # print("#            [ Alunos ]               #")
    # print("#                                     #")
    # print("#   Cod[1]: Cadastrar Aluno           #")
    # print("#   Cod[2]: Listar / Alterar Aluno    #")
    # print("#   Cod[3]: Pesquisar Aluno           #")
    # print("# ----------------------------------- #")
    # print("#          [ Professores ]            #")
    # print("#                                     #")
    # print("#   Cod[4]: Cadastrar Professor       #")
    # print("#   Cod[5]: Listar / Alterar Prof.    #")
    # print("#   Cod[6]: Pesquisar Professor       #")
    # print("# ----------------------------------- #")
    # print("#         [ Outras opções ]           #")
    # print("#                                     #")
    # print("#   Cod[7]: Listar                    #")
    # print("#   Cod[8]: Pesquisar                 #")
    # print("# ----------------------------------- #")
    # print("#                                     #")
    # print("#   Cod[9]: Sair                      #")
    # print("#   Cod[0]: Sobre                     #")
    # print("#                                     #")
    # print("#######################################\n")

# Aprimoramentos:
# 1- Função isValid:
#   - Receber listas e realizar validações
#   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções do menu e coisas do tipo
#   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos
#
# 2- Notas alunos:
# - Tratar entrada notas, é uma lista de int, atualmente está entrando como notas individuais, fazer que seja possível entrar: 8.5, 7.3, 9
# e realizar o tratamento para separar as notas e adicionar ou atualizar no Json

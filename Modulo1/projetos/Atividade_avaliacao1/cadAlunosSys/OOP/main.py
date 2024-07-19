##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####
##### Ricardo Nogueira ####

import funcoesSuporte as func


# Controle Menu Principal:
while True:

  # Exibir menu principal:
  opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu = func.exibirMenuPrincipal()

  if opcaoMenuPrincipal == 1:
    func.telaCadastroAluno()
  elif opcaoMenuPrincipal == 2:
    func.listarAlunos()
  elif opcaoMenuPrincipal == 3:
    func.pesquisar()
  elif opcaoMenuPrincipal == 4:
    func.sair()
    break
  elif opcaoMenuPrincipal == 5:
    func.sobre()
  else:
    print("Opção inválida. Tente novamente.")



# Aprimoramentos:
# 1- Função isValid:
#   - Receber listas e realizar validações
#   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções do menu e coisas do tipo
#   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos
#
# 2- Notas alunos:
# - Tratar entrada notas, é uma lista de int, atualmente está entrando como notas individuais, fazer que seja possível entrar: 8.5, 7.3, 9
# e realizar o tratamento para separar as notas e adicionar ou atualizar no Json
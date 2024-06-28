##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####

import funcoesSuporte


# Controle Menu Principal:
while True:

  # Exibir menu principal:
  opcaoMenuPrincipal, erroTipoMenu, erroVazioMenu, erroMsgMenu = funcoesSuporte.exibirMenuPrincipal()

  if opcaoMenuPrincipal == 1:
    funcoesSuporte.telaCadastroAluno()
  elif opcaoMenuPrincipal == 2:
    opcaoMenuAlterarExcluir = funcoesSuporte.listarAlunos()
  elif opcaoMenuPrincipal == 3:
    funcoesSuporte.sair()
    break
  elif opcaoMenuPrincipal == 4:
    funcoesSuporte.sobre()
  else:
    print("Opção inválida. Tente novamente.")



# Faltando fazer:
# - 1 - Tratar entrada notas, é uma lista de int, atualmente está entrando como notas individuais, fazer que seja possível entrar: 8.5, 7.3, 9
# e realizar o tratamento para separar as notas e adicionar ou atualizar no Json
#
# Aprimoramentos:
# 1- Função isValid:
#   - Receber listas e realizar validações
#   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções a fins
#   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos



# Json backup teste:
# {
#   "Alunos": [
#     {
#       "id": 1,
#       "nome": "João da Silva",
#       "curso": "Ciência da Computação",
#       "matricula": 2023001,
#       "notas": [8.5, 7.0, 9.0],
#       "presencas": 18,
#       "telefone": "1234-5678",
#       "email": "joao.silva@email.com"
#     },
#     {
#       "id": 2,
#       "nome": "Maria Oliveira",
#       "curso": "Engenharia Civil",
#       "matricula": 2023002,
#       "notas": [9.5, 8.0, 10.0],
#       "presencas": 20,
#       "telefone": "9876-5432",
#       "email": "maria.oliveira@email.com"
#     },
#     {
#       "id": 3,
#       "nome": "Pedro Santos",
#       "curso": "Administração",
#       "matricula": 2023003,
#       "notas": [6.0, 7.5, 8.5],
#       "presencas": 15,
#       "telefone": "5555-1111",
#       "email": "pedro.santos@email.com"
#     }
#   ]
# }
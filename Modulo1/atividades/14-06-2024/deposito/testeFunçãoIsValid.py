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
  


'''
Testes:
'''
valor, erroTipo, erroVazio, erroMsg = isValidInput("Digite um nome: ", "string")
print(f"valor: {valor} - tipoValor: {type(valor)} - erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

valor, erroTipo, erroVazio, erroMsg = isValidInput("Digite um número inteiro: ", "int")
print(f"valor: {valor} - tipoValor: {type(valor)} - erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

valor, erroTipo, erroVazio, erroMsg = isValidInput("Digite um número real: ", "float")
print(f"valor: {valor} - tipoValor: {type(valor)} - erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

valor, erroTipo, erroVazio, erroMsg = isValidInput("Digite um número: ", "intFloat")
print(f"valor: {valor} - tipoValor: {type(valor)} - erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

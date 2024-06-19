# - msg: mensagem mostrada no input
# - tipoEspera: "string", "int", "float", "intFloat" - "intFloat" podendo receber int ou float
# aceitaVazio: padrão False (não aceitando valors vazios), caso aceite, declarar na chamada da função como True
# - Retorno da função: erroTipo, erroVazio, msgErro

def isValidInput(msg, tipoEsperado, aceitaVazio = False):
  # Inicialização dos erros:
  erroTipo = False
  erroVazio = False
  erroMsg = ""

  while True:
    valor = input(msg)
    # Verifica se está vazio e se deveria estar
    if (aceitaVazio == False) and (len(valor) == 0):
      erroMsg = "Entrada vazia não é permitida."
      erroVazio = True
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
      elif (tipoEsperado == "float"):
        try:
            valor = float(valor)
            erroTipo = False
            break
        except ValueError:
            erroTipo = True
            erroMsg = "Entrada inválida. O valor deve ser um float."
      elif (tipoEsperado == "intFloat"):
        try:
            valor = float(valor)
            erroTipo = False
            break
        except ValueError:
            erroTipo = True
            erroMsg = "Entrada inválida. O valor deve ser um número."

  return erroTipo, erroVazio, erroMsg
  


'''
Testes:
'''
erroTipo, erroVazio, erroMsg = isValidInput("Digite um número: ", "intFloat")
print(f"erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

erroTipo, erroVazio, erroMsg = isValidInput("Digite um nome: ", "string")
print(f"erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

erroTipo, erroVazio, erroMsg = isValidInput("Digite um número real: ", "float")
print(f"erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")

erroTipo, erroVazio, erroMsg = isValidInput("Digite um número inteiro: ", "int")
print(f"erroTipo: {erroTipo} - erroVazio: {erroVazio} - erroMsg: {erroMsg}")
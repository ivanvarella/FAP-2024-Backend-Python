import re

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

# Função para tratar a temp separando o valor da escala e validando
def trataTemp(tempUser):
  while True:
    # Comando match da biblioteca re, usando expressões regulares para tratar a string.
    # Aceitando somente início da string como números (inteiros ou reais) e o final com somente 1 caractere sendo C,F,K,c,f ou k.
    # Retornando um objeto match já com as partes "capturadas" com a expressão regular
    match = re.match(r"^(-?\d+(\.\d+)?)([CFKcfk])$", tempUser)

    if match:
      valorTemp = float(match.group(1))
      escalaTemp = match.group(3).upper()
      # O return além de retornar os valores, também funciona como o break para o while
      return valorTemp, escalaTemp
    else:
      print("Entrada inválida! Certifique-se de usar um número seguido de 'C', 'F' ou 'K'. Ex: 100C, 1800K, 32F.")

# Função para tratar a escala escolhida pelo usuário usando expressões regulares
def trataEscala(escalaDesejada):
  while True:
    # Verifica se a entrada é uma das letras válidas (C, F, K) ignorando maiúsculas/minúsculas
    if re.match(r"^[CFKcfk]$", escalaDesejada):
      return escalaDesejada.upper()
    else:
      print("Entrada inválida! Certifique-se de digitar 'C', 'F' ou 'K'.")

# Função para escolher a conversão e executa-la (Cod. 0)
def escolheEConverte(tempConversao, escalaConversao, escalaConvertida):
  if (escalaConversao == "C") and (escalaConvertida == "F"):
    msgConversao = "Conversão de Celsius para Fahrenheit"
    tempConvertida = CelsiusToFahrenheit(tempConversao)
    return tempConvertida, msgConversao
  elif (escalaConversao == "C") and (escalaConvertida == "K"):
    msgConversao = "Conversão de Celsius para Kelvin"
    tempConvertida = CelsiusToKelvin(tempConversao)
    return tempConvertida, msgConversao
  elif (escalaConversao == "F") and (escalaConvertida == "C"):
    msgConversao = "Conversão de Fahrenheit para Celsius"
    tempConvertida = FahrenheitToCelsius(tempConversao)
    return tempConvertida, msgConversao
  elif (escalaConversao == "F") and (escalaConvertida == "K"):
    msgConversao = "Conversão de Fahrenheit para Kelvin"
    tempConvertida = FahrenheitToKelvin(tempConversao)
    return tempConvertida, msgConversao
  elif (escalaConversao == "K") and (escalaConvertida == "C"):
    msgConversao = "Conversão de Kelvin para Celsius"
    tempConvertida = KelvinToCelsius(tempConversao)
    return tempConvertida, msgConversao
  elif (escalaConversao == "K") and (escalaConvertida == "F"):
    msgConversao = "Conversão de Kelvin para Fahrenheit"
    tempConvertida = KelvinToFahrenheit(tempConversao)
    return tempConvertida, msgConversao

# Funções de conversão de escalas cod.: 1 - 6
def CelsiusToFahrenheit(celsius):
  return round((celsius * 9/5) + 32, 2)
def CelsiusToKelvin(celsius):
  return round(celsius + 273.15, 2)
def FahrenheitToCelsius(fahrenheit):
  return round((fahrenheit - 32) * 5/9, 2)
def FahrenheitToKelvin(fahrenheit):
  return round((fahrenheit - 32) * 5/9 + 273.15, 2)
def KelvinToCelsius(kelvin):
  return round(kelvin - 273.15, 2)
def KelvinToFahrenheit(kelvin):
  return round((kelvin - 273.15) * 9/5 + 32, 2)

# Função para exibir o resultado da conversão
def exibeConversao(msgConversao, tempConversao, tempConvertida, escala1, escala2):
   print(f"\n\n--------------- {msgConversao} -----------------------\n")
   print(f"Temperatura {tempConversao} {escala1} é equivamente a {tempConvertida} {escala2}.\n")



'''
Exemplos interessantes:

Expressão regulares:

Contexto
Os códigos value = float(match.group(1)) e scale = match.group(3).upper() são usados para extrair e manipular as partes específicas da entrada do usuário depois que a expressão regular encontrou uma correspondência válida.

O que é match
Quando a expressão regular re.match(r"^(-?\d+(\.\d+)?)([CFKcfk])$", user_input) encontra uma correspondência na string user_input, ela retorna um objeto match. Este objeto contém grupos de captura, que são partes específicas da string que foram capturadas pelos parênteses na expressão regular.

Grupos de Captura na Expressão Regular
A expressão regular r"^(-?\d+(\.\d+)?)([CFKcfk])$" tem três grupos de captura:

(-?\d+(\.\d+)?)

-? : Captura um sinal de negativo opcional.
\d+ : Captura um ou mais dígitos (a parte inteira do número).
(\.\d+)? : Captura um ponto decimal seguido de um ou mais dígitos (a parte fracionária do número), se presente.
Este grupo captura o valor numérico completo da temperatura, seja ele um inteiro ou um número decimal, positivo ou negativo.

(\.\d+)?

Este é um grupo dentro do primeiro grupo, capturando apenas a parte decimal do número (se presente).
([CFKcfk])

Captura a letra que representa a escala de temperatura (Celsius, Fahrenheit ou Kelvin), aceitando tanto maiúsculas quanto minúsculas.
Extração dos Grupos Capturados
Agora vamos detalhar os códigos específicos:

value = float(match.group(1))
match.group(1):
group(1) refere-se ao primeiro grupo de captura da expressão regular, que é (-?\d+(\.\d+)?).
Este grupo captura a parte numérica da entrada do usuário.
float(...):
Converte a string capturada pelo grupo em um número de ponto flutuante (float).
Isso é necessário porque a entrada do usuário é inicialmente uma string, e precisamos de um número para realizar operações matemáticas.
scale = match.group(3).upper()
match.group(3):
group(3) refere-se ao terceiro grupo de captura, que é ([CFKcfk]).
Este grupo captura a letra que indica a escala de temperatura.
.upper():
Converte a letra capturada para maiúscula.
Isso é feito para garantir uniformidade, já que a entrada do usuário pode ser em maiúscula ou minúscula, mas é mais fácil de manipular se for padronizada (por exemplo, sempre em maiúscula).
Resumo
value = float(match.group(1)) converte a parte numérica da entrada do usuário em um número de ponto flutuante.
scale = match.group(3).upper() extrai a escala de temperatura (C, F ou K) e a converte para maiúscula para facilitar o processamento posterior.
Esses códigos juntos permitem que você extraia e normalize a entrada do usuário para uso posterior no programa.

'''
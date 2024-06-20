##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####

import funcoesSuporte

print("\n++++  Cálculo da capacidade de um depósito  ++++\n\n")

print("######## Tabela de conversão #######")
print("# [Cod. 0] Digitar a temperatura   #")
print("# [Cod. 1] Celsius para Fahrenheit #")
print("# [Cod. 2] Celsius para Kelvin     #")
print("# [Cod. 3] Fahrenheit para Celsius #")
print("# [Cod. 4] Fahrenheit para Kelvin  #")
print("# [Cod. 5] Kelvin para Celsius     #")
print("# [Cod. 6] Kelvin para Fahrenheit  #")
print("####################################")

while True:
    msg = "\nEscolha uma opção segundo a tabela acima: "
    escalaTemp, erroTipoEscalaTemp, erroVazioEscalaTemp, erroMsgEscalaTemp = funcoesSuporte.isValidInput(msg, "int")
    if (escalaTemp >= 0) and (escalaTemp <= 6):
        break
    else:
        print("Por favor digite valores entre 0 e 6 segundo a tabela acima!")

# Verifica se o usuário escolheu o Cod da tabela ou digitou a temperatura com a escala
if escalaTemp == 0:
    # Retira os espaços, se houverem, do início e final da string
    tempUser = input("Digite a temperatura com a escala (ex: 100C, 1800K, 32F): ").strip()
    # Função valida e trata o valor do input
    tempConversao, escalaConversao = funcoesSuporte.trataTemp(tempUser)
    # Verifica se as escalas são iguais
    while True:
        escalaDesejada = input("Digite a escala de conversão desejada (ex: C, F, K): ").strip()
        # Função valida e trata a escala para conversão
        escalaConvertida = funcoesSuporte.trataEscala(escalaDesejada)
        if (escalaConversao == escalaConvertida):
            print("A escala de conversão deve ser diferente da de origem!")
        else:
            break
    # Função para escolher a função de conversão e executar-la
    tempConvertida, msgConversao = funcoesSuporte.escolheEConverte(tempConversao, escalaConversao, escalaConvertida)
    funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, escalaConversao, escalaConvertida)
else:
    if (escalaTemp == 1):
        msgConversao = "Conversão de Celsius para Fahrenheit"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Celsius (ex.: 100): ", "float")
        tempConvertida = funcoesSuporte.CelsiusToFahrenheit(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "C", "F")
    elif (escalaTemp == 2):
        msgConversao = "Conversão de Celsius para Kelvin"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Celsius (ex.: 100): ", "float")
        tempConvertida = funcoesSuporte.CelsiusToKelvin(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "C", "K")
    elif (escalaTemp == 3):
        msgConversao = "Conversão de Fahrenheit para Celsius"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Fahrenheit (ex.: 32): ", "float")
        tempConvertida = funcoesSuporte.FahrenheitToCelsius(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "F", "C")
    elif (escalaTemp == 4):
        msgConversao = "Conversão de Fahrenheit para Kelvin"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Fahrenheit (ex.: 32): ", "float")
        tempConvertida = funcoesSuporte.FahrenheitToKelvin(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "F", "K")
    elif (escalaTemp == 5):
        msgConversao = "Conversão de Kelvin para Celsius"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Kelvin (ex.: 1800): ", "float")
        tempConvertida = funcoesSuporte.KelvinToCelsius(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "K", "C")
    elif (escalaTemp == 6):
        msgConversao = "Conversão de Kelvin para Fahrenheit"
        tempConversao, erroTipoTempConversao, erroVazioTempConversao, erroMsgTempConversao = funcoesSuporte.isValidInput("Digite a temperatura em Kelvin (ex.: 1800): ", "float")
        tempConvertida = funcoesSuporte.KelvinToFahrenheit(tempConversao)
        funcoesSuporte.exibeConversao(msgConversao, tempConversao, tempConvertida, "K", "F")



'''
msg = "\nEscolha a escala segundo a tabela acima ou digite a temperatura incluindo a escala (ex: 100C, 1800K, 32F: "


1 - Melhorar a função isValid: inserir possibilidade de range quando for int, float ou intFloat
'''
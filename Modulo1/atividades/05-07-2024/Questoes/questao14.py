# Questão 14(Questão 5 da parte 2):
# Desenvolva uma função que receba uma string e a comprima, substituindo
# sequências de caracteres repetidos por um número seguido do caractere (por
# exemplo, "aaabbbcccc" se tornaria "3a3b4c").

import funcoesSuporte


def compimirString(string):
    # Verifica se a string está vazia
    if not string:
        return ""

    stringComprimida = []
    countRepeticao = 1

    # Começa a partir do segundo caractere (for i in range(1, len(string)):) porque se compara cada caracter com o anterior para contar as repetições consecutivas.
    # Se a iteração começasse a partir do primeiro caractere (for i in range(0, len(string)):), a comparação s[i] == s[i - 1] na primeira iteração (i = 0) 
    # causaria um erro de índice, pois s[i - 1] tentaria acessar s[-1], que se refere ao último caractere da string em Python, e não a um índice anterior válido.

    # Itera sobre a string a partir do segundo caractere, para cada caracter:
    for char in range(1, len(string)):
        # Se a anterior for igual: conta uma repetição
        if string[char] == string[char - 1]:
            countRepeticao += 1
        # Acabou a repetição: guarda o número de repetições e o caractere anterior, já que o atual é diferente
        else:
            stringComprimida.append(f"{countRepeticao}{string[char - 1]}")
            countRepeticao = 1

    # Adiciona o último grupo de caracteres
    stringComprimida.append(f"{countRepeticao}{string[-1]}")

    # Transforma a lista em uma string contínua
    return "".join(stringComprimida)


def descomprimirString(string):
    # Verifica se a string está vazia
    if not string:
        return ""

    stringDescomprimida = []
    countRepeticao = ''

    for char in string:
        # verifica se o caractere é um digito, se True guarda (pois pode ter mais de um dígito, exemplo: 12a)
        if char.isdigit():
            countRepeticao += char
        # Quando não for um dígito, guarda o caractere e multiplica pela quantidade de repetições: int(countRepeticao)
        else:
            stringDescomprimida.append(char * int(countRepeticao))
            # Reseta o contador de repetições para o próximo caractere
            countRepeticao = ''
    # Transforma a lista em string contínua
    return ''.join(stringDescomprimida)


while True:
    opcao, erroTipoOpcao, erroVazioOpcao, erroMsgOpcao = funcoesSuporte.isValidInput("\n\nDigite 1 para comprimir ou 2 para descomprimir uma string: ", "int")
    if opcao == 1 or opcao == 2:
        break
    print("\nOpção inválida. Tente novamente.")

if opcao == 1:
    stringInput, erroTipoStringInput, erroVazioStringInput, erroMsgStringInput = funcoesSuporte.isValidInput("\n\nDigite uma string para ser comprimida: ", "string")
    stringComprimida = compimirString(stringInput)
    print(f"\nA string comprimida é: {stringComprimida}\n")
elif opcao == 2:
    stringInput, erroTipoStringInput, erroVazioStringInput, erroMsgStringInput = funcoesSuporte.isValidInput("\n\nDigite uma string para ser descomprimida: ", "string")
    stringDescomprimida = descomprimirString(stringInput)
    print(f"\nA string descomprimida é: {stringDescomprimida}\n")
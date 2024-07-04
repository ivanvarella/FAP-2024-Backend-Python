# Questão 10(Questão 1 da parte 2):
# Crie uma função que receba uma string e retorne uma nova string com todas as
# vogais removidas.

import funcoesSuporte

def removeVogais(string):
    vogais = "aeiouAEIOU"
    stringSemVogais = ""
    # Percorre toda a string
    for char in string:
        # Só adiciona se não for vogal, ou seja, se NÃO estiver no vogais = "aeiouAEIOU"
        if char not in vogais:
            stringSemVogais += char
    return stringSemVogais

# String aceita tudo, porém sempre trata como string
string, erroTipoString, erroVazioString, erroMsgString = funcoesSuporte.isValidInput("Digite uma string para remoção das vogais: ", "string")

stringSemVogais = removeVogais(string)

print(stringSemVogais)
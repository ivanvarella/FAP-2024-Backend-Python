# Questão 12(Questão 3 da parte 2):
# Crie um programa que receba uma frase e a "criptografe" movendo cada letra 3
# posições para frente no alfabeto (por exemplo, 'a' se torna 'd', 'z' se torna 'c').

# Exemplo funcionamento algoritmo circular: Pegar 4 na frente, levando em consideração o algoritomo circular.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tamanhoLista = len(lista) # tamanhoLista = 9
# IndiceInicial = 7 # Ou seja, lista[7] = 8
# proximoIndice = (IndiceInicial + 4) % tamanhoLista # Ou seja, proximoIndice = (7 + 4) % 9, proximoIndice = 11 % 9 = 2
# # Com isso podemos ver que o próximo valor (4 na frente do algoritmo circular) será o 2, sendo o valor igual a 3 (lista[3])
# # Para ser possível a implementação do algoritmo circular, é necessário saber o tamanho da pilha que se irá percorrer.

import funcoesSuporte

def criptografar(string):
    alfabetoMinusculo = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMaiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = []
    
    # Percorre cada caracter
    for char in string:
        if char.islower():  # Verifica se é uma letra minúscula
            indiceOriginal = alfabetoMinusculo.index(char)
            # Aplica o algorítimo circular: Utiliza o módulo (%) para garantir que quando passar de 26 (indiceOriginal + 3), 
            # retorne o resto, que será utilizado para somar no início da fila circular
            novoIndice = (indiceOriginal + 3) % 26
            novaLetra = alfabetoMinusculo[novoIndice]
            resultado.append(novaLetra)
        elif char.isupper():  # Verifica se é uma letra maiúscula
            indiceOriginal = alfabetoMaiusculo.index(char)
            novoIndice = (indiceOriginal + 3) % 26
            novaLetra = alfabetoMaiusculo[novoIndice]
            resultado.append(novaLetra)
        else:
            resultado.append(char)  # Não altera caracteres não alfabéticos
    # Transforma a lista resultado em uma string única, com separador igual a '', 
    # ou seja, sem espaços entre a string.
    # Porém, os espaços originalmente incluidos na string, serão adicionados \
    # normalmente, pois são ignorados na função.
    return ''.join(resultado)


string, erroTipoString, erroVazioString, erroMsgString = funcoesSuporte.isValidInput("Digite uma string para ser criptografada: ", "string")
stringCriptogradafa = criptografar(string)
print(f"A string criptografada é: {stringCriptogradafa}")
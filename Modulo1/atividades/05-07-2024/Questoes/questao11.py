# Questão 11(Questão 2 da parte 2):
# 2. Implemente um programa que conte o número de ocorrências de cada palavra
# em uma frase, ignorando maiúsculas/minúsculas e pontuação.

import os

# Caminho padrão para os arquivos
caminhoPastaPadrao = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/arquivos/"
caminhoArquivo = caminhoPastaPadrao + "LoremIpsum.txt"

def carregaTxt(caminhoArquivo):
  with open(caminhoArquivo, 'r', encoding='utf-8') as file:
    texto = file.readlines()
  return texto

# Função para remover toda a pontuação do texto e dividir em palavras
def limparDividirTexto(texto):
    # Define caracteres de pontuação
    pontuacoes = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    textoSemPontuacao = ""
    
    for char in texto:
        # Se não estiver na lista de pontuacoes, guarda o caracter
        if char not in pontuacoes:
            textoSemPontuacao += char.lower() # Todo o texto em minúsculo
        else:
            textoSemPontuacao += ' '  # Substitui pontuações por espaços para separar palavras
    
    # Divide o texto em palavras
    # .split(): divide a string em palavras separadas por espaços
    palavras = textoSemPontuacao.split()
    return palavras


texto = carregaTxt(caminhoArquivo)

numLinhas = len(texto)

# A expressão abaixo é uma expressão geradora e pode ser reescrita da seguinte forma:
# numPalavras = 0
# for linha in linhas:
#   numPalavras += len(linha.split())
# Ou seja,numPalavras está recebendo os valores de len(linha.split()), 
# que por sua vez está sendo executado dentro do for linha in linhas
numPalavras = sum(len(linha.split()) for linha in texto)
numCaracteres = sum(len(linha) for linha in texto)

# Converte para string (garantia que será string). split() divide a string em uma lista com separador, no caso sem separador
palavras = limparDividirTexto(texto)

# Contagem de ocorrências de cada palavra da lista palavras, cria o dicionário ocorrencias onde, se existir a palavra ele 
# soma a ococrrencia da paplavra, se não tiver a palavra, cria a chave com a palavra e soma +1 no valor.
ocorrencias = {}
for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

# Exibir o número de ocorrências de cada palavra
print("\n\nNúmero de ocorrências de cada palavra:")
for palavra, contagem in ocorrencias.items():
    print(f"{palavra}: {contagem}")

print("\n -------  Informações sobre o texto analizado ------- ")
print(f"\nNúmero de linhas: {numLinhas}")
print(f"\nNúmero de palavras: {numPalavras}")
print(f"\nNúmero de caracteres: {numCaracteres}")
print("-" * 53 + "\n\n")
# Questão 16 (Questão 7 da parte 2):
# Escreva um programa que leia um arquivo de texto e conte o número de linhas,
# palavras e caracteres.

import os
import funcoesSuporte
# pip install python-docx
from docx import Document

# Caminho padrão para os arquivos
caminhoPastaPadrao = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/arquivos/"

def contarLinhasPalavrasCaracteres(caminhoArquivo):
    # Separa a extensão do restante da string
    restanteString, extensaoArquivo = os.path.splitext(caminhoArquivo)

    if extensaoArquivo == '.txt':
        with open(caminhoArquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
        
        numLinhas = len(linhas)
        # .split(): divide a string em palavras separadas por espaços
        # A expressão abaixo é uma expressão geradora e pode ser reescrita da seguinte forma:
        # numPalavras = 0
        # for linha in linhas:
        #   numPalavras += len(linha.split())
        # Ou seja,numPalavras está recebendo os valores de len(linha.split()), 
        # que por sua vez está sendo executado dentro do for linha in linhas
        numPalavras = sum(len(linha.split()) for linha in linhas)
        numCaracteres = sum(len(linha) for linha in linhas)

    elif extensaoArquivo == '.docx':
        doc = Document(caminhoArquivo)
        linhas = []

        for paragrafo in doc.paragraphs:
            linhas.extend(paragrafo.text.strip().split('\n'))

        numLinhas = len(linhas)
        numPalavras = sum(len(linha.split()) for linha in linhas)
        numCaracteres = sum(len(linha) for linha in linhas)

    else:
        print(f"Formato de arquivo não suportado: {extensaoArquivo}")
        return None, None, None
    
    return numLinhas, numPalavras, numCaracteres

print(f"\n\nO caminho padrão para os arquivos é o: {caminhoPastaPadrao}\n")
arquivo, erroTipoArquivo, erroVazioArquivo, erroMsgArquivo = funcoesSuporte.isValidInput("Digite o nome do arquivo (incluindo sua extensão .txt ou .docx): ", "string")
caminhoArquivo = caminhoPastaPadrao + arquivo

linhas, palavras, caracteres = contarLinhasPalavrasCaracteres(caminhoArquivo)

if linhas is not None:
    print(f"Número de linhas: {linhas}")
    print(f"Número de palavras: {palavras}")
    print(f"Número de caracteres: {caracteres}")
else:
    print("Ocorreu um erro ao processar o arquivo.")

# Exemplos:
# LoremIpsum.txt
# LoremIpsum.docx
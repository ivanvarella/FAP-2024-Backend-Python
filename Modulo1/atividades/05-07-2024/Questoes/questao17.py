# Questão 17(Questão 8 da parte 2):
# 8. Crie um script que copie o conteúdo de um arquivo para outro, mantendo a
# formatação original.

import os

# Caminho padrão para os arquivos
caminhoPastaPadrao = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/arquivos/"

arquivoOrigem = "LoremIpsum.txt"
caminhoArquivoOrigem = caminhoPastaPadrao + arquivoOrigem

arquivoDestino = "questao17.txt"
caminhoArquivoDestino = caminhoPastaPadrao + arquivoDestino


def carregaArquivoOrigem(caminhoArquivoOrigem):
  with open(caminhoArquivoOrigem, 'r', encoding='utf-8') as file:
    texto = file.read()
    return texto
  
def copiaArquivoDestino(caminhoArquivoDestino, texto):
  with open(caminhoArquivoDestino, 'w', encoding='utf-8') as file:
    file.write(texto)

def limparArquivoTxt(caminhoArquivoDestino):
  with open(caminhoArquivoDestino, 'w', encoding='utf-8') as file:
      # Grava uma string vazia para limpar o conteúdo do arquivo
      # Também poderia somente executar o comando pass, ou seja, não fazer nada, pois,
      # quando se confgura o arquivo para ser gravado e não se faz nada, nenhuma gravação,
      # ele é gravado com vazio.
      # Porém, prefiro utilizar o método write abaixo por deixar mais clara a intenção do código.
      file.write("")

# Limpa o código de destino
limparArquivoTxt(caminhoArquivoDestino)

# Carregando o arquivo destino:
texto = carregaArquivoOrigem(caminhoArquivoOrigem)

# Copiando para o arquivo destino:
copiaArquivoDestino(caminhoArquivoDestino, texto)
# Questão 19(Questão 10 da parte 2):
# 10. Desenvolva um programa que mescle dados de dois arquivos CSV diferentes em
# um terceiro arquivo.

# Biblioteca padrão do python para lidar com arquivos CSV
import csv
import os

# Caminho padrão para os arquivos
caminhoPastaPadrao = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/arquivos/"

# Caminho do arquivo CSV 1
arquivoCsv1 = 'questao18.csv'

# Caminho do arquivo CSV 2
arquivoCsv2 = 'questao19_original.csv'

# Caminho do arquivo CSV mesclado - Inicialmente vazio
arquivoCsvMesclado = 'questao19_mesclado.csv'

caminhoCompletoArquivoCsv1 = caminhoPastaPadrao + arquivoCsv1
caminhoCompletoArquivoCsv2 = caminhoPastaPadrao + arquivoCsv2
caminhoCompletoAquivoCsvMesclado = caminhoPastaPadrao + arquivoCsvMesclado

def carregaMesclaArquivosCsv(caminhoCsv1, caminhoCsv2, caminhoCsvMesclado):
    try:
      # Abrir e ler o primeiro arquivo CSV
      with open(caminhoCsv1, newline='', encoding='utf-8') as csvfile1:
        leitorCsv1 = csv.reader(csvfile1, delimiter=',')
        linhas_mescladas = list(leitorCsv1)  # Adicionar linhas do primeiro CSV

      # Abrir e ler o segundo arquivo CSV
      with open(caminhoCsv2, newline='', encoding='utf-8') as csvfile2:
        leitorCsv2 = csv.reader(csvfile2, delimiter=',')
        next(leitorCsv2)  # Pular cabeçalho do segundo CSV
        linhas_mescladas.extend(list(leitorCsv2))  # Adicionar linhas do segundo CSV
      
      # Escrever as linhas mescladas no arquivo CSV de saída
      with open(caminhoCsvMesclado, 'w', newline='', encoding='utf-8') as csvfileMesclado:
        escritorCsv = csv.writer(csvfileMesclado)
        for linha in linhas_mescladas:
          escritorCsv.writerow(linha)

      print(f"\n\nArquivos '{arquivoCsv1}' e '{arquivoCsv2}' mesclados com sucesso em '{arquivoCsvMesclado}'.\n")

    except FileNotFoundError as e:
      print(f"Erro: Arquivo não encontrado - {e.filename}")
    
    except Exception as e:
      print(f"Ocorreu um erro ao mesclar os arquivos: {e}")

def exibirCsv(caminhoCompletoArquivo, arquivoCsv):
  try:
    with open(caminhoCompletoArquivo, newline='', encoding='utf-8') as csvfile:
      leitorCsv = csv.reader(csvfile, delimiter=',')  # Cria um objeto leitor de CSV

      # Lê o cabeçalho
      cabeçalho = next(leitorCsv)
      # numeroColunas = len(cabeçalho)

      # Contar o número de linhas
      # numeroLinhas = sum(1 for linha in leitorCsv)

      # Calcula as larguras máximas das colunas, utilizando para formatar a exibição
      larguras = [0] * len(cabeçalho)

      # Itera pelas linhas do arquivo CSV (dados) para calcular as larguras
      for linha in leitorCsv:
        for i, item in enumerate(linha):
          larguras[i] = max(larguras[i], len(item))

      # Reinicia a leitura do arquivo para imprimir novamente
      csvfile.seek(0)
      next(leitorCsv)  # Pula o cabeçalho

      # Imprime o cabeçalho formatado
      # O '^' é um especificador de alinhamento, para ficar centralizado. Então o item será formatado utilizando :^{lagura} -> centralizado dentro da largura calculada
      print(" | ".join(f"{item:^{largura}}" for item, largura in zip(cabeçalho, larguras)))
      print("-" * (sum(larguras) + len(larguras) * 3 - 1))

      # Itera pelas linhas do arquivo CSV (dados) para imprimir cada linha formatada
      for linha in leitorCsv:
        # O método .zip() combina elementos de várias iteráveis em tuplas
        # Exemplo:
        # linha = ["João", "25", "São Paulo", "Engenheiro"]
        # larguras = [5, 2, 9, 11]
        # Primeira iteração:
        # item = "João" e largura = 5
        # E o output para o .zip(linha, larguras) seria a tupla: ("Nome", "João")
        # Segunda iteração:
        # item = "25" e largura = 2
        # E o output para o .zip(linha, larguras) seria a tupla: ("Idade", "25")
        print(" | ".join(f"{item:^{largura}}" for item, largura in zip(linha, larguras)))

  # Exceção expecífica quando não encontrar o arquivo ou não consegui acessa-lo
  except FileNotFoundError:
    print(f"Arquivo '{arquivoCsv}' não encontrado no caminho: {caminhoPastaPadrao}.")
  # Exceção genérica para qualquer outro tipo de erro
  except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")

def linhasColunas(caminhoCompletoArquivo, arquivoCsv):
  try:
    with open(caminhoCompletoArquivo, newline='', encoding='utf-8') as csvfile:
      leitorCsv = csv.reader(csvfile, delimiter=',')  # Cria um objeto leitor de CSV

      # Lê o cabeçalho
      cabeçalho = next(leitorCsv)
      numeroColunas = len(cabeçalho)

      # Contar o número de linhas
      numeroLinhas = sum(1 for linha in leitorCsv)

  # Exceção expecífica quando não encontrar o arquivo ou não consegui acessa-lo
  except FileNotFoundError:
    print(f"Arquivo '{arquivoCsv}' não encontrado no caminho: {caminhoPastaPadrao}.")
  # Exceção genérica para qualquer outro tipo de erro
  except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")

  return numeroLinhas, numeroColunas

carregaMesclaArquivosCsv(caminhoCompletoArquivoCsv1, caminhoCompletoArquivoCsv2, caminhoCompletoAquivoCsvMesclado)

print(f"\n\nConteúdo do arquivo CSV mesclado: {arquivoCsvMesclado}\n")
exibirCsv(caminhoCompletoAquivoCsvMesclado, arquivoCsvMesclado)
numeroLinhas, numeroColunas = linhasColunas(caminhoCompletoAquivoCsvMesclado, arquivoCsvMesclado)
print(f"Número de linhas: {numeroLinhas} | Número de colunas: {numeroColunas}\n")
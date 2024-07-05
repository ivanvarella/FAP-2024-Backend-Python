# Questão 18(Questão 9 da parte 2):
# 9. Desenvolva um programa que leia um arquivo CSV e imprima seu conteúdo
# formatado na tela.

# Biblioteca padrão do python para lidar com arquivos CSV
import csv
import os

# Caminho padrão para os arquivos
caminhoPastaPadrao = os.getcwd() + "/Modulo1/atividades/05-07-2024/Questoes/arquivos/"

# Caminho do arquivo CSV
arquivoCsv = 'questao18.csv'

caminhoCompletoArquivo = caminhoPastaPadrao + arquivoCsv

def carregaExibeArquivoCsv(caminhoCompletoArquivo):
    try:
      with open(caminhoCompletoArquivo, newline='', encoding='utf-8') as csvfile:
        leitorCsv = csv.reader(csvfile, delimiter=',')  # Cria um objeto leitor de CSV

        # Lê o cabeçalho
        cabeçalho = next(leitorCsv)

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

# Executa a função para ler arquivo CSV e exibir seu conteúdo formatado
print(f"\n\nConteúdo do arquivo CSV: {arquivoCsv}\n")
carregaExibeArquivoCsv(caminhoCompletoArquivo)


# Conteúdo do aquivo csv - criado na pasta arquivos como questao18.csv:

# Nome,Idade,Cidade,Profissao
# João,25,São Paulo,Engenheiro
# Maria,30,Rio de Janeiro,Médica
# Pedro,28,Porto Alegre,Advogado
# Ana,22,Belo Horizonte,Professor
# Carlos,35,Brasília,Contador
# Juliana,27,Salvador,Arquiteta
# Lucas,29,Recife,Programador
# Isabela,26,Fortaleza,Jornalista
# Gustavo,32,Florianópolis,Designer
# Carolina,31,Manaus,Enfermeira
# Rafael,33,Curitiba,Empresário
# Amanda,24,Goiania,Psicóloga
# Marcos,36,Porto Velho,Veterinário
# Mariana,23,Natal,Bióloga
# Thiago,29,Cuiabá,Analista de Sistemas
# Beatriz,27,João Pessoa,Estudante
# Felipe,30,Teresina,Consultor Financeiro
# Patricia,28,Aracaju,Farmacêutica
# Rodrigo,34,Palmas,Engenheiro Civil
# Laura,25,Vitória,Advogada
# Fernando,26,Maceió,Professor Universitário
# Gabriela,31,Boa Vista,Engenheira de Software
# Eduardo,32,Campo Grande,Médico Veterinário
# Vanessa,29,Macapá,Psicopedagoga
# Daniel,27,São Luís,Empreendedor
# Camila,33,Rio Branco,Artesã
# Henrique,28,Anápolis,Analista de Marketing
# Tatiane,30,Joinville,Nutricionista
# Paulo,34,Porto Seguro,Corretor de Imóveis
# Julia,26,Ilhéus,Esteticista
# Anderson,31,Santarém,Engenheiro Eletricista
# Larissa,29,Marabá,Fisioterapeuta
# Leonardo,35,Barreiras,Pedagogo
# Renata,27,Itabuna,Advogada Trabalhista
# Mateus,33,Feira de Santana,Designer Gráfico
# Débora,28,Teixeira de Freitas,Pediatra
# Bruno,30,Alagoinhas,Gestor de Projetos
# Carla,32,Lauro de Freitas,Engenheira Ambiental
# Luciana,29,Simões Filho,Professora de Inglês
# Marcia,34,Paulo Afonso,Psicóloga Clínica
# Roberto,25,Itabira,Analista Financeiro
# Silvia,26,São José do Rio Preto,Arquiteto
# Ricardo,31,Londrina,Professor de Matemática
# Vanessa,27,Marília,Biomédica
# Alexandre,33,Presidente Prudente,Administrador
# Sabrina,28,Sorocaba,Enfermeiro
# Jorge,30,Araraquara,Gerente de Vendas
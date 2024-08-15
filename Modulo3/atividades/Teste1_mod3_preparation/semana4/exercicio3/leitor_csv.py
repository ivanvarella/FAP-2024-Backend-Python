import csv
import os

# Define o caminho para o diretório do projeto
caminho_base = os.getcwd()
caminho_projeto = os.path.join(
    caminho_base,
    "Modulo3",
    "atividades",
    "Teste1_mod3_preparation",
    "semana4",
    "exercicio3",
)


def ler_arquivo_csv(caminho_arquivo):
    """Lê um arquivo CSV e retorna uma lista de dicionários onde cada dicionário representa uma linha do CSV,
    e uma lista com todos os departamentos únicos."""
    departamentos_unicos = set()
    dados = []

    with open(caminho_arquivo, mode="r", encoding="utf-8") as file:
        leitor = csv.DictReader(file)

        for linha in leitor:
            dados.append(linha)
            # Adiciona o departamento ao set para garantir unicidade
            departamentos_unicos.add(linha["Departamento"].strip().lower())

    # Converte o set para uma lista
    lista_departamentos = list(departamentos_unicos)
    return dados, lista_departamentos


def obter_nomes_por_departamento(dados, departamento_desejado):
    """Filtra os funcionários de um departamento específico e retorna uma lista com seus nomes."""
    departamento_desejado = departamento_desejado.strip().lower()
    nomes = [
        funcionario["Nome"]
        for funcionario in dados
        if funcionario["Departamento"].strip().lower() == departamento_desejado
    ]
    return nomes


def main(caminho):
    caminho_arquivo = os.path.join(
        caminho, "dados.csv"
    )  # Substitua pelo caminho do seu arquivo CSV

    # Lê os dados do arquivo CSV e obtém a lista de departamentos únicos
    dados_funcionarios, lista_departamentos = ler_arquivo_csv(caminho_arquivo)

    # Imprimir os departamentos que existem:
    print("-" * 40)
    print("Departamentos disponíveis:")
    print("-" * 40)
    for departamento in lista_departamentos:
        print(departamento)
    print("-" * 40)

    departamento_desejado = input("\n\nDigite o nome do departamento a ser filtrado: ")

    # Obtém os nomes dos funcionários do departamento desejado
    nomes = obter_nomes_por_departamento(dados_funcionarios, departamento_desejado)

    if nomes:
        print(f"Nomes dos funcionários do departamento '{departamento_desejado}':")
        for nome in nomes:
            print(nome)
    else:
        print(
            f"Nenhum funcionário encontrado no departamento '{departamento_desejado}'."
        )


main(caminho_projeto)

import os

caminho_base = os.getcwd()
caminho_projeto = os.path.join(
    caminho_base,
    "Modulo3",
    "atividades",
    "Teste1_mod3_preparation",
    "semana4",
    "exercicio2",
)
caminho_arquivo = os.path.join(caminho_projeto, "texto.txt")


def contar_linhas_palavras_caracteres(caminho):
    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()  # Retorna uma lista com as linhas
        num_linhas = len(linhas)

        arquivo.seek(0)  # Retonado o ponteiro para o início do arquivo
        texto = arquivo.read()
        num_palavras = len(texto.split())
        num_caracteres = len(texto)

    return num_linhas, num_palavras, num_caracteres


def criar_novo_txt(caminho, num_linhas, num_palavras, num_caracteres):
    # Criar o arquivo ou sobrescrever o existente
    caminho_arquivo_resultado = os.path.join(caminho, "resultado.txt")
    with open(caminho_arquivo_resultado, "w") as novo_arquivo:
        novo_arquivo.write(
            f"O arquivo possui {num_linhas} linhas, {num_palavras} palavras e {num_caracteres} caracteres.\n"
        )


def main(caminho_arquivo):
    num_linhas, num_palavras, num_caracteres = contar_linhas_palavras_caracteres(
        caminho_arquivo
    )
    print("\n\nArquivo carregado e processado!\n")
    criar_novo_txt(caminho_projeto, num_linhas, num_palavras, num_caracteres)
    print("Resultado gravado em 'resultado.txt'\n\n")


main(caminho_arquivo)

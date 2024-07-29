# sudo apt-get install xdg-utils
# sudo apt install firefox -> porque o WSL não possui navegador

import os
import platform

# Caminho do diretório atual
caminhoPastaPadrao = os.getcwd()
caminho = os.path.join(
    caminhoPastaPadrao,
    "Modulo1",
    "projetos",
    "Atividade_avaliacao1",
    "cadAlunosSys",
    "OOP",
)

# O HTML será gravado no diretório raiz
arquivo_html = os.path.join(caminho, "dados.html")


def gera_html(arquivo_html, alunos):
    # Criando o arquivo HTML caso não exista
    with open(arquivo_html, "w", encoding="utf-8") as html:
        html.write(
            """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Dados dos Alunos</title>
        <style>
        .image-container {
            text-align: center;
        }
        .image-container img {
            max-width: 500px;
            height: auto;
            display: block;
            margin: 0 auto;
            margin-bottom: 20px;
        }
        </style>
        </head>
        <body>
        <div class="image-container">
        """
        )

        for aluno in alunos:
            html.write(
                f"""
            <h2>{aluno["nome"]}</h2>
            <p>Idade: {aluno["idade"]}</p>
            <p>Nota: {aluno["nota"]}</p>
            <hr>
            """
            )

        html.write(
            """
        </div>
        </body>
        </html>
        """
        )


# Abre um link ou o arquivo html no navegador padrão
def abrir_link(url):
    if platform.system() == "Windows":
        os.system(f"start {url}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {url}")
    else:  # Linux
        os.system(f"xdg-open {url}")
        # Brs para mover os warnings do xdg-open
        # Enquanto o navegador estiver aberto o terminal ficará "travado" com a instância do xdg-open
        # só será efetivo quando fechar
        print("\n\n\n\n\n\n\n\n\n\n")


# ============================================


# Usando as funções criadas


# Lista de alunos (exemplo)
alunos = [
    {"nome": "Alice", "idade": 20, "nota": 8.5},
    {"nome": "Bob", "idade": 22, "nota": 7.8},
    {"nome": "Carol", "idade": 21, "nota": 9.1},
]

gera_html(arquivo_html, alunos)

# url = "https://www.google.com"  # Tem que ter o "https://" ou o "http://"
url = arquivo_html
# print(f"Acesse o site clicando no link: {url}")

# Abrir o html no navegador padrão do sistema
abrir_link(url)

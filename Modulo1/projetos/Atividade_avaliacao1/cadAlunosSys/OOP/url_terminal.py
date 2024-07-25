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


# =============================================================================


# Criando o arquivo HTML
# with open(arquivo_html, "w", encoding="utf-8") as página:
#     página.write(
#         """
#     <!DOCTYPE html>
#     <html lang="pt-BR">
#     <head>
#     <meta charset="utf-8">
#     <title>Imagens</title>
#     <style>
#     .image-container {
#         text-align: center;
#     }
#     .image-container img {
#         max-width: 500px;
#         height: auto;
#         display: block;
#         margin: 0 auto;
#         margin-bottom: 20px;
#     }
#     </style>
#     </head>
#     <body>
#     <div class="image-container">
#     """
#     )

#     for nome, caminho in imagens_dict.items():
#         # página.write(f'<img src="{caminho}" class="media-object img-thumbnail">\n')
#         página.write(
#             f'<a href="{caminho}"><img src="{caminho}" class="media-object img-responsive img-thumbnail"></a>\n'
#         )

#     página.write(
#         """
#     </div>
#     </body>
#     </html>
#     """
#     )


# ============================================


def abrir_link(url):
    if platform.system() == "Windows":
        os.system(f"start {url}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {url}")
    else:  # Linux
        os.system(f"xdg-open {url}")


url = "www.google.com"
# url = arquivo_html
print(f"Acesse o site clicando no link: {url}")

# Abrir o html no navegador padrão do sistema
abrir_link(url)

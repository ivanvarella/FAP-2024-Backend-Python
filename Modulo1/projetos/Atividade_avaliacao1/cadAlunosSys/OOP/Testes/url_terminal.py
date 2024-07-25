# sudo apt-get install xdg-utils
# sudo apt install firefox -> porque o WSL não possui navegador

import os
import platform


def abrir_link(url):
    if platform.system() == "Windows":
        os.system(f"start {url}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {url}")
    else:  # Linux
        os.system(f"xdg-open {url}")


url = "https://www.google.com"
print(f"Acesse o site clicando no link: {url}")

# Descomente a linha abaixo se quiser abrir o link automaticamente
abrir_link(url)


# =============================================================================

import os

# Caminho para o diretório de imagens
caminhoPastaImagens = os.path.join(os.getcwd(), "arquivos", "img")

# O HTML será gravado no diretório raiz, as imagens ficarão em outra pasta separada
arquivo_html_img = os.path.join(os.getcwd(), "arquivos", "img.html")

# Dicionário para armazenar nome da imagem e caminho completo
imagens_dict = {}

# Percorre os arquivos no diretório de imagens
for nome_arquivo in os.listdir(caminhoPastaImagens):
    caminho_completo = os.path.join(caminhoPastaImagens, nome_arquivo)
    if os.path.isfile(caminho_completo):  # Verifica se é um arquivo
        imagens_dict[nome_arquivo] = caminho_completo

# Criando o arquivo HTML
with open(arquivo_html_img, "w", encoding="utf-8") as página:
    página.write(
        """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="utf-8">
    <title>Imagens</title>
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

    for nome, caminho in imagens_dict.items():
        # página.write(f'<img src="{caminho}" class="media-object img-thumbnail">\n')
        página.write(
            f'<a href="{caminho}"><img src="{caminho}" class="media-object img-responsive img-thumbnail"></a>\n'
        )

    página.write(
        """
    </div>
    </body>
    </html>
    """
    )

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

import flet as ft


def main(pagina: ft.Page):
    # Cabeçalho simples
    pagina.title = "Teste Básico com Flet"

    # Exibe uma mensagem ao carregar a página
    pagina.add(ft.Text("Bem-vindo à aplicação Flet!", size=24, color=ft.colors.BLUE))

    # Campo de texto
    campo_texto = ft.TextField(label="Digite algo", width=300)

    # Função chamada ao clicar no botão
    def ao_clicar(evento):
        pagina.add(ft.Text(f"Você digitou: {campo_texto.value}", color=ft.colors.GREEN))

    # Botão que chama a função ao ser clicado
    botao = ft.ElevatedButton(text="Clique aqui", on_click=ao_clicar)

    # Adicionando o campo de texto e o botão à página
    pagina.add(campo_texto, botao)


# Rodando a aplicação no navegador
# ft.app(target=main, port=8000)
# ft.app(target=main, port=8000)
# ft.app(target=main)
# ft.app(target=main, view=ft.WEB)
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

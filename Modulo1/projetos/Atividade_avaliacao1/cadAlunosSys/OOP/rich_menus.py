# rich_menus.py

from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box
from rich.live import Live
from contextlib import contextmanager
from typing import Generator
import time


def principal_rich1():
    console = Console()
    table = Table(
        title="\n\n\n\n\n\n\n\n[not italic bold]:chart_increasing: Menu Principal :chart_decreasing:[/]",
        style="yellow bold",
        show_header=True,
        header_style="bold white",
    )
    codigo = Text("Cod", style="cyan", justify="center")
    opcao = Text("Opção", style="green", justify="center")
    linha_pequena = Text("-" * 10, style="yellow bold", justify="center")
    linha_grande = Text("-" * 40, style="yellow bold", justify="center")

    table.add_column(codigo, no_wrap=True, style="cyan")
    table.add_column(opcao, style="green")
    alunos = Text("[Alunos]", style="green", justify="center")
    table.add_row("", alunos)
    table.add_row("", "")
    table.add_row("Cod[ 1]", "Cadastrar Aluno")
    table.add_row("Cod[ 2]", "Listar / Alterar / Excluir Aluno")
    table.add_row("Cod[ 3]", "Pesquisar Aluno")
    table.add_row("", "")
    table.add_row(linha_pequena, linha_grande)
    professores = Text("[Professores]", style="green", justify="center")
    table.add_row("", professores)
    table.add_row("", "")
    table.add_row("Cod[ 4]", "Cadastrar Professor")
    table.add_row("Cod[ 5]", "Listar / Alterar / Excluir Professor")
    table.add_row("Cod[ 6]", "Pesquisar Professor")
    table.add_row("", "")
    table.add_row(linha_pequena, linha_grande)
    outras_opcoes = Text("[Outras Opções]", style="green", justify="center")
    table.add_row("", outras_opcoes)
    table.add_row("", "")
    table.add_row("Cod[ 7]", "Listar")
    table.add_row("Cod[ 8]", "Pesquisar")
    table.add_row("Cod[ 9]", "Dados no Navegador")
    table.add_row("Cod[10]", "Gerar PDF com os Dados")
    table.add_row("", "")
    table.add_row(linha_pequena, linha_grande)
    table.add_row("", "")
    table.add_row("Cod[11]", "Sair")
    table.add_row("Cod[ 0]", "Sobre")
    table.add_row("", "")

    console.print(table)


def principal_rich2():
    """Menu animado usando Live"""
    alunos = Text("[Alunos]", style="green bold", justify="center")
    professores = Text("[Professores]", style="green bold", justify="center")
    outras_opcoes = Text("[Outras Opções]", style="green bold", justify="center")

    codigo = Text("Cod", style="cyan bold", justify="center")
    opcao = Text("Opção", style="green bold", justify="center")
    linha_pequena = Text("-" * 10, style="yellow bold", justify="center")
    linha_grande = Text("-" * 40, style="yellow bold", justify="center")

    TABLE_DATA = [
        ["", alunos],
        ["Cod: [ 1]", "Cadastrar Aluno"],
        ["Cod: [ 2]", "Listar / Alterar / excluir"],
        ["Cod: [ 3]", "Pesquisar Aluno"],
        [linha_pequena, linha_grande],
        ["", ""],
        ["", professores],
        ["Cod: [ 4]", "Cadastrar Professor"],
        ["Cod: [ 5]", "Listar / Alterar / Excluir"],
        ["Cod: [ 6]", "Pesquisar Professor"],
        [linha_pequena, linha_grande],
        ["", ""],
        ["", outras_opcoes],
        ["Cod: [ 7]", "Listar"],
        ["Cod: [ 8]", "Pesquisar"],
        ["Cod: [ 9]", "Dados no navegador"],
        ["Cod: [10]", "Gerar PDF com os dados"],
        [linha_pequena, linha_grande],
        ["", ""],
        ["Cod: [11]", "Sair"],
        ["Cod: [ 0]", "Sobre"],
        ["", ""],
    ]

    console = Console()
    BEAT_TIME = 0.01

    @contextmanager
    def beat(length: int = 1) -> Generator[None, None, None]:
        yield
        time.sleep(length * BEAT_TIME)

    table = Table(show_footer=False, box=box.SIMPLE)
    table.add_column("Código", style="cyan bold", justify="center")
    table.add_column("Opção", style="green bold")

    console.clear()

    with Live(table, console=console, screen=False, refresh_per_second=120):
        with beat(5):
            table.title = "[not italic]:chart_increasing:[/] Menu Principal [not italic]:chart_decreasing:[/]"

        for row in TABLE_DATA:
            with beat(5):
                table.add_row(*row)

        with beat(4):
            table.border_style = "bright_yellow"
            table.row_styles = ["none", "dim"]
            table.columns[0].header_style = "bold cyan"
            table.columns[1].header_style = "bold green"
            table.columns[0].style = "cyan"
            table.columns[1].style = "green"
            table.columns[0].justify = "center"
            table.columns[1].justify = "left"

        original_width = console.measure(table).maximum

        for width in range(original_width, console.width, 2):
            with beat(1):
                table.width = width

        for width in range(console.width, original_width, -2):
            with beat(1):
                table.width = width

        for width in range(original_width, 90, -2):
            with beat(1):
                table.width = width

        for width in range(90, original_width + 1, 2):
            with beat(1):
                table.width = width

        with beat(2):
            table.width = None


# # Teste as funções
# if __name__ == "__main__":
#     # principal_rich1()
#     principal_rich2()  # Comente esta linha para evitar execução não desejada

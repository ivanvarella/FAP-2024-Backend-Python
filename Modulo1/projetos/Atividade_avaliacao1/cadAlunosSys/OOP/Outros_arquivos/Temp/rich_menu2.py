"""Same as the table_movie.py but uses Live to update"""

import time
from contextlib import contextmanager

from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text

# Dados da tabela
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
    ["Cod: [10]", "Gera PDF com os dados"],
    [linha_pequena, linha_grande],
    ["", ""],
    ["Cod: [11]", "Sair"],
    ["Cod: [ 0]", "Sobre"],
    ["", ""],
]

console = Console()

BEAT_TIME = 0.01


@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)


# Criação da tabela
table = Table(show_footer=False, box=box.SIMPLE)

# Configuração das colunas
table.add_column("Código", style="cyan bold", justify="center")
table.add_column("Opção", style="green bold")

console.clear()

with Live(table, console=console, screen=False, refresh_per_second=120):
    with beat(12):
        table.title = "[not italic]:chart_increasing:[/] Menu Principal [not italic]:chart_decreasing:[/]"

    # Adicionar linhas
    for row in TABLE_DATA:
        with beat(12):
            table.add_row(*row)

    # Aplicar estilos às colunas e linhas
    with beat(10):
        table.border_style = "bright_yellow"
        table.row_styles = ["none", "dim"]
        table.columns[0].header_style = "bold cyan"
        table.columns[1].header_style = "bold green"
        table.columns[0].style = "cyan"
        table.columns[1].style = "green"
        table.columns[0].justify = "center"
        table.columns[1].justify = "left"

    # Ajustar largura da tabela
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

import time
from contextlib import contextmanager

from rich import box
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

# Dados da tabela
TABLE_DATA_ALUNO = [
    ["Cod: [1]", "Cadastrar Aluno"],
    ["Cod[2]", "Listar / Alterar / excluir"],
    ["Cod[3]", "Pesquisar Aluno"],
]

TABLE_DATA_PROFESSOR = [
    ["Cod[4]", "Cadastrar Professor"],
    ["Cod[5]", "Listar / Alterar / Excluir"],
    ["Cod[6]", "Pesquisar Professor"],
]

TABLE_DATA_OUTRAS_OPCOES = [
    ["Cod[7]", "Listar"],
    ["Cod[8]", "Pesquisar"],
    ["Cod[9]", "Dados no navegador"],
    ["Cod[10]", "Gera PDF com os dados"],
]

TABLE_DATA_PROGRAMA = [
    ["Cod[11]", "Sair"],
    ["Cod[0]", "Sobre"],
]

console = Console()

BEAT_TIME = 0.04


@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)


def create_table(title, data):
    table = Table(show_footer=False, box=box.SIMPLE, show_edge=False, expand=True)
    table.add_column("Código", style="cyan", justify="center")
    table.add_column("Opção", style="magenta")
    table.title = title

    for row in data:
        table.add_row(*row)

    return table


console.clear()

with Live(console=console, screen=False, refresh_per_second=20):
    with beat(10):
        table_aluno = create_table("Menu Principal - Alunos", TABLE_DATA_ALUNO)

    with beat(10):
        table_professor = create_table(
            "Menu Principal - Professores", TABLE_DATA_PROFESSOR
        )

    with beat(10):
        table_outras_opcoes = create_table(
            "Menu Principal - Outras Opções", TABLE_DATA_OUTRAS_OPCOES
        )

    with beat(10):
        table_programa = create_table("Menu Principal - Programa", TABLE_DATA_PROGRAMA)

    panels = [
        Panel(table_aluno, box=box.MINIMAL),
        Panel(table_professor, box=box.MINIMAL),
        Panel(table_outras_opcoes, box=box.MINIMAL),
        Panel(table_programa, box=box.MINIMAL),
    ]

    for panel in panels:
        console.print(panel)

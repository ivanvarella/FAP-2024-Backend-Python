import sqlite3
import os
from datetime import datetime

# Caminho para o banco de dados SQLite onde as tarefas serão armazenadas
CAMINHO_BANCO = os.path.join(os.getcwd(), "Avant", "tarefas.db")


def conectar():
    """Estabelece uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DataIn TEXT NOT NULL,
            DataFim TEXT,
            Descricao TEXT NOT NULL,
            prioridade INTEGER,
            status INTEGER,
            obs TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def carregar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, DataIn, DataFim, Descricao, prioridade, status, obs FROM tarefas"
    )
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


def salvar_tarefa(descricao, prioridade, status, datain=None, datafim=None, obs=None):
    conn = conectar()
    cursor = conn.cursor()
    if status is not None:
        if status == 3:  # Status 3 = Concluída
            datafim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if datain is None:
        datain = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        """
        INSERT INTO tarefas (DataIn, DataFim, Descricao, prioridade, status, obs)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (datain, datafim, descricao, prioridade, status, obs),
    )
    conn.commit()
    conn.close()


def atualizar_tarefa(id, status=None, obs=None, datafim=None):
    conn = conectar()
    cursor = conn.cursor()

    if status is not None:
        if status == 3:  # Status 3 = Concluída
            datafim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            """
            UPDATE tarefas SET status = ?, DataFim = ? WHERE id = ?
        """,
            (status, datafim, id),
        )

    if obs is not None:
        cursor.execute(
            """
            UPDATE tarefas SET obs = ? WHERE id = ?
        """,
            (obs, id),
        )

    conn.commit()
    conn.close()


def excluir_tarefa_db(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, (id, datain, datafim, descricao, prioridade, status, obs) in enumerate(
            tarefas, 1
        ):
            print(f"{i}. {descricao} - Prioridade: {prioridade}, Status: {status}")
            print(
                f"   Data de Início: {datain}, Data de Fim: {datafim}, Observações: {obs}"
            )


def adicionar_tarefa(
    descricao, prioridade, status, datain=None, datafim=None, obs=None
):
    salvar_tarefa(descricao, prioridade, status, datain, datafim, obs)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")


def mudar_status_tarefa(indice):
    tarefas = carregar_tarefas()
    try:
        id = tarefas[indice - 1][0]
        status_atual = tarefas[indice - 1][5]
        obs_atual = tarefas[indice - 1][6]

        print(f"Status atual: {status_atual}")
        novo_status = input(
            "Digite o novo status (1: Pendente, 2: Iniciado, 3: Concluído, 4: Excluído): "
        )

        novo_status = int(novo_status) if novo_status else status_atual

        nova_obs = input(f"Digite novas observações (atual: {obs_atual}): ")
        nova_obs = nova_obs if nova_obs else obs_atual

        atualizar_tarefa(id, status=novo_status, obs=nova_obs)
        print(f"Tarefa {indice} atualizada com sucesso!")
    except IndexError:
        print("Índice de tarefa inválido.")


def excluir_tarefa(indice):
    tarefas = carregar_tarefas()
    try:
        id = tarefas[indice - 1][0]
        excluir_tarefa_db(id)
        print(f"Tarefa '{tarefas[indice - 1][3]}' excluída com sucesso!")
    except IndexError:
        print("Índice de tarefa inválido.")


def mostrar_ajuda():
    print("Comandos disponíveis:")
    print("  adicionar 'descricao' 'prioridade' 'status' - Adiciona uma nova tarefa.")
    print("  listar                                    - Lista todas as tarefas.")
    print(
        "  mudar_status N                            - Altera o status e observações da tarefa N."
    )
    print("  excluir N                                 - Exclui a tarefa N.")
    print("  ajuda                                     - Mostra este menu de ajuda.")


def mostrar_menu():
    print("Gerenciador de Tarefas")
    print("1 - Listar todas as tarefas")
    print("2 - Adicionar uma nova tarefa")
    print("3 - Mudar status de uma tarefa")
    print("4 - Excluir uma tarefa")
    print("5 - Ajuda")
    print("6 - Sair")
    print("Digite 'ajuda' para ver os comandos disponíveis.")


def main():
    print("Bem-vindo ao Gerenciador de Tarefas - Avant!")
    criar_tabela()  # Cria a tabela caso não exista
    mostrar_menu()
    opcoes_menu = [1, 2, 3, 4, 5, 6]
    while True:
        try:
            comando = int(input("Digite um comando: "))
            if comando not in opcoes_menu:
                raise ValueError
        except ValueError:
            print("Comando inválido. Tente novamente.")
            continue

        if comando == 1:
            listar_tarefas()
        elif comando == 2:
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = int(input("Digite a prioridade (1 a 5): "))
            status = int(
                input(
                    "Digite o status (1: Pendente, 2: Iniciado, 3: Concluído, 4: Excluído): "
                )
            )
            observacoes = input("Digite as observações (opcional): ")
            observacoes = observacoes if observacoes else None
            adicionar_tarefa(descricao, prioridade, status, obs=observacoes)
        elif comando == 3:
            indice = int(input("Digite o número da tarefa que deseja concluir: "))
            mudar_status_tarefa(indice)
        elif comando == 4:
            indice = int(input("Digite o número da tarefa que deseja excluir: "))
            excluir_tarefa(indice)
        elif comando == 5:
            mostrar_ajuda()
        elif comando == 6:
            break
        else:
            print("Comando inválido. Tente novamente.")


if __name__ == "__main__":
    main()

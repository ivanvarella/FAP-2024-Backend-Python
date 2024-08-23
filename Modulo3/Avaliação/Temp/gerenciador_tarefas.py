import sqlite3
from datetime import datetime
import os

# Obtém o caminho completo do diretório onde o arquivo atual está localizado
caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
# Caminho para o banco de dados SQLite onde as tarefas serão armazenadas
CAMINHO_BANCO = os.path.join(caminho_diretorio, "tarefas.db")


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


def carregar_tarefas(query):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


def salvar_tarefa(descricao, prioridade, status, datain=None, datafim=None, obs=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO tarefas (DataIn, DataFim, Descricao, prioridade, status, obs)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (datain, datafim, descricao, prioridade, status, obs),
    )
    conn.commit()
    conn.close()


def atualizar_tarefa(id, descricao, status, obs=None, datafim=None):
    conn = conectar()
    cursor = conn.cursor()

    # Iniciar a construção do comando SQL
    sql = "UPDATE tarefas SET"
    params = []

    # Atualiza o campo Descricao
    sql += " Descricao = ?,"
    params.append(descricao)

    # Atualiza o campo Status
    sql += " status = ?,"
    params.append(status)

    # Atualiza o campo DataFim se status for 3
    if status == 3:  # Status 3 = Concluída
        datafim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if datafim is not None:
        sql += " DataFim = ?,"
        params.append(datafim)

    # Atualiza o campo Observações
    if obs is not None:
        sql += " obs = ?,"
        params.append(obs)

    # Remover a vírgula extra do final da string SQL
    sql = sql.rstrip(",")

    # Adicionar a cláusula WHERE
    sql += " WHERE id = ?"
    params.append(id)
    # print(sql, params)
    input("Pressione Enter para continuar...")

    # Executar o comando SQL
    cursor.execute(sql, tuple(params))
    conn.commit()
    conn.close()


def limpar_terminal():
    # Verifica o sistema operacional
    if os.name == "nt":  # Se for Windows
        os.system("cls")
    else:  # Se for Linux ou macOS
        os.system("clear")


def excluir_tarefa_db(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def listar_tarefas(query):
    limpar_terminal()
    tarefas = carregar_tarefas(query)
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nTarefas:")
        print(
            "------------------------------------------------------------------------------------------------------------------------"
        )
        for i, (id, datain, datafim, descricao, prioridade, status, obs) in enumerate(
            tarefas, 1
        ):
            print(
                f"\nID {id} - {descricao} - Prioridade: {prioridade}, Status: {status}"
            )
            print(
                f"   Data de Início: {datain}, Data de Fim: {datafim}, Observações: {obs}\n"
            )
        print(
            "------------------------------------------------------------------------------------------------------------------------\n"
        )


def adicionar_tarefa(descricao, prioridade, status, obs=None):
    if status == 3:  # Status 3 = Concluída
        datafim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        datafim = None
    datain = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    salvar_tarefa(descricao, prioridade, status, datain, datafim, obs)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")
    input("Pressione Enter para continuar...")


def editar_tarefa(id):

    # tarefas -> Lista de tuplas, exemplo: [(1, '2024-08-16 14:15:17', None, 'teste', 4, 1, None)]
    tarefas = carregar_tarefas(f"SELECT * FROM tarefas WHERE id = {id}")

    if tarefas:
        descricao_atual = tarefas[0][3]
        status_atual = tarefas[0][5]  # Sempre primeira tupla (nesse caso, única tupla)
        obs_atual = tarefas[0][6]
        prioridade = tarefas[0][4]

        print(f"\nDescrição atual: {descricao_atual}")
        nova_descricao = input("Digite a nova descrição ou Enter para manter a atual: ")
        nova_descricao = nova_descricao if nova_descricao else descricao_atual

        print(f"\nStatus atual: {status_atual}")
        novo_status = input(
            "Digite o novo status ou Enter para manter o atual(1: Pendente, 2: Iniciado, 3: Concluído, 4: Excluído): "
        )
        novo_status = int(novo_status) if novo_status else status_atual
        if novo_status == 3:  # Status 3 = Concluída
            dataFim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            dataFim = None

        print(f"\nPrioridade atual: {prioridade}")
        nova_prioridade = input(
            "Digite a nova prioridade (1 a 3) ou Enter para manter a atual: "
        )
        nova_prioridade = int(nova_prioridade) if nova_prioridade else prioridade

        print(f"\nObservações atuais: {obs_atual}")
        nova_obs = input(f"Digite novas observações ou Enter para manter a atual: ")
        nova_obs = nova_obs if nova_obs else obs_atual

        atualizar_tarefa(
            id,
            descricao=nova_descricao,
            status=novo_status,
            obs=nova_obs,
            datafim=dataFim,
        )
        print(f"Tarefa com ID {id} atualizada com sucesso!")
        input("Pressione Enter para continuar...")
    else:
        print("ID de tarefa inválido.")


def excluir_tarefa(id):
    excluir_tarefa_db(id)
    print(f"Tarefa com ID {id} excluída com sucesso!")
    input("\nPressione Enter para continuar...")


def sobre():
    limpar_terminal()
    print("Gerenciador de Tarefas - Avant")
    print("Desenvolvido por: Ivan Varella")
    print("Versão: 1.0")
    print("Data: 2023-06-01")
    print("Licença: MIT License\n")
    input("Pressione Enter para voltar ao menu principal...")
    limpar_terminal()
    mostrar_menu()


def mostrar_menu():
    print("Gerenciador de Tarefas")
    print("1 - Listar todas as tarefas")
    print("2 - Adicionar uma nova tarefa")
    print("3 - Editar uma tarefa")
    print("4 - Excluir uma tarefa")
    print("5 - Sobre")
    print("6 - Sair")


def main():
    print("Bem-vindo ao Gerenciador de Tarefas - Avant!")
    # criar_tabela()  # Cria a tabela caso não exista
    mostrar_menu()
    opcoes_menu = [1, 2, 3, 4, 5, 6]
    prioridades = [1, 2, 3]
    status_disponiveis = [1, 2, 3, 4]
    while True:
        try:
            comando = int(input("Digite um comando: "))
            if comando not in opcoes_menu:
                raise ValueError
        except ValueError:
            print("Comando inválido. Tente novamente.")
            continue

        if comando == 1:  # 1- Listar
            limpar_terminal()
            listar_tarefas("SELECT * FROM tarefas")
            mostrar_menu()
        elif comando == 2:  # 2- Adicionar
            limpar_terminal()
            print("\n# Adicionar nova tarefa #\n")
            descricao = input("Digite a descrição da tarefa: ")
            while True:
                try:
                    prioridade = int(input("Digite a prioridade (1 a 3): "))
                    if prioridade not in prioridades:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Prioridade inválida. Tente novamente.")

            while True:
                try:
                    status = int(
                        input(
                            "Digite o status (1: Pendente, 2: Iniciado, 3: Concluído, 4: Excluído): "
                        )
                    )
                    if status not in status_disponiveis:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Status inválido. Tente novamente.")
            observacoes = input(
                "Digite as observações (opcional) ou Enter para continuar: "
            )
            observacoes = observacoes if observacoes else None
            adicionar_tarefa(descricao, prioridade, status, obs=observacoes)
            limpar_terminal()
            mostrar_menu()
        elif comando == 3:  # 3- Editar tarefa
            limpar_terminal()
            listar_tarefas("SELECT * FROM tarefas")
            id = int(input("Digite o ID da tarefa que deseja alterar: "))
            editar_tarefa(id)
            limpar_terminal()
            mostrar_menu()
        elif comando == 4:  # 4- Excluir tarefa
            limpar_terminal()
            listar_tarefas("SELECT * FROM tarefas")
            id = int(input("Digite o ID da tarefa que deseja excluir: "))
            excluir_tarefa(id)
            limpar_terminal()
            mostrar_menu()
        elif comando == 5:
            sobre()
        elif comando == 6:
            limpar_terminal()
            break
        else:
            print("Comando inválido. Tente novamente.")


if __name__ == "__main__":
    main()

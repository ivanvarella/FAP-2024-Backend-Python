import json
import os


# Caminho para o arquivo JSON onde as tarefas serão armazenadas
CAMINHO_ARQUIVO = os.path.join(os.getcwd(), "tarefas.json")


def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as file:
            return json.load(file)
    return []


def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(CAMINHO_ARQUIVO, "w") as file:
        json.dump(tarefas, file, indent=4)


def listar_tarefas():
    """Lista todas as tarefas."""
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['titulo']} - {status}")


def adicionar_tarefa(titulo):
    """Adiciona uma nova tarefa."""
    tarefas = carregar_tarefas()
    nova_tarefa = {"titulo": titulo, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


def marcar_como_concluida(indice):
    """Marca uma tarefa como concluída."""
    tarefas = carregar_tarefas()
    try:
        tarefas[indice - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print(f"Tarefa {indice} marcada como concluída!")
    except IndexError:
        print("Índice de tarefa inválido.")


def excluir_tarefa(indice):
    """Exclui uma tarefa."""
    tarefas = carregar_tarefas()
    try:
        tarefa_excluida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_excluida['titulo']}' excluída com sucesso!")
    except IndexError:
        print("Índice de tarefa inválido.")


def mostrar_ajuda():
    """Mostra as instruções de uso."""
    print("Comandos disponíveis:")
    print("  adicionar 'nome da tarefa' - Adiciona uma nova tarefa.")
    print("  listar                   - Lista todas as tarefas.")
    print("  concluir N               - Marca a tarefa N como concluída.")
    print("  excluir N                - Exclui a tarefa N.")
    print("  ajuda                    - Mostra este menu de ajuda.")


def main():
    import sys

    if len(sys.argv) < 2:
        mostrar_ajuda()
        return

    comando = sys.argv[1].lower()

    if comando == "adicionar":
        if len(sys.argv) < 3:
            print("Erro: O nome da tarefa é obrigatório.")
        else:
            adicionar_tarefa(" ".join(sys.argv[2:]))

    elif comando == "listar":
        listar_tarefas()

    elif comando == "concluir":
        if len(sys.argv) < 3:
            print("Erro: O número da tarefa é obrigatório.")
        else:
            try:
                indice = int(sys.argv[2])
                marcar_como_concluida(indice)
            except ValueError:
                print("Erro: O número da tarefa deve ser um número inteiro.")

    elif comando == "excluir":
        if len(sys.argv) < 3:
            print("Erro: O número da tarefa é obrigatório.")
        else:
            try:
                indice = int(sys.argv[2])
                excluir_tarefa(indice)
            except ValueError:
                print("Erro: O número da tarefa deve ser um número inteiro.")

    elif comando == "ajuda":
        mostrar_ajuda()

    else:
        print(f"Comando desconhecido: {comando}")
        mostrar_ajuda()


main()

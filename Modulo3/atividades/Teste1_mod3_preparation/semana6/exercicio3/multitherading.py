import threading
import time
import os

caminho_base = os.getcwd()
caminho_projeto = os.path.join(
    caminho_base,
    "Modulo3",
    "atividades",
    "Teste1_mod3_preparation",
    "semana6",
    "exercicio3",
)
caminho_arquivo = os.path.join(caminho_projeto, "texto.txt")


# Função para ler um arquivo
def ler_arquivo(caminho_arquivo):
    start_time = time.time()  # Registrar o tempo de início
    try:
        with open(caminho_arquivo, "r") as file:
            conteudo = file.read()
            print("Conteúdo do arquivo lido com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    end_time = time.time()  # Registrar o tempo de fim
    print(f"Tempo de leitura do arquivo: {end_time - start_time:.2f} segundos")


# Função para calcular a soma de uma lista de números
def calcular_soma(lista_numeros):
    start_time = time.time()  # Registrar o tempo de início
    soma = sum(lista_numeros)
    end_time = time.time()  # Registrar o tempo de fim
    print(f"A soma dos números é: {soma}")
    print(f"Tempo de cálculo da soma: {end_time - start_time:.2f} segundos")


def main(caminho_arquivo):
    # Definir a lista de números
    lista_numeros = list(
        range(1, 100000001)
    )  # Lista com números de 1 a 100.000.000.000

    # Criar threads para as duas tarefas
    thread_arquivo = threading.Thread(target=ler_arquivo, args=(caminho_arquivo,))
    thread_soma = threading.Thread(target=calcular_soma, args=(lista_numeros,))

    # Iniciar as threads
    thread_arquivo.start()
    thread_soma.start()

    # Esperar que ambas as threads terminem
    thread_arquivo.join()
    thread_soma.join()

    print("Ambas as tarefas foram concluídas.")


main(caminho_arquivo)

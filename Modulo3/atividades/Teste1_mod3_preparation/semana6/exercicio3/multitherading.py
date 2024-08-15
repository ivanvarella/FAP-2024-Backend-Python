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

# Código antigo, explicação do possível problema:
# Você está certo em notar que algo parece estar errado com os resultados. Vamos analisar os possíveis problemas e sugerir algumas correções:

# Problema de concorrência: As threads estão compartilhando o mesmo console para impressão, o que pode causar sobreposição de saídas e tempos imprecisos.
# Granularidade do tempo: A função time.time() pode não ter resolução suficiente para medir operações muito rápidas.
# Overhead de criação de threads: Para tarefas muito rápidas, o overhead de criar e gerenciar threads pode superar os benefícios do paralelismo.
# GIL (Global Interpreter Lock): Em CPython, o GIL pode impedir a execução verdadeiramente paralela de threads para operações ligadas à CPU.
# # Função para ler um arquivo
# def ler_arquivo(caminho_arquivo):
#     start_time = time.time()  # Registrar o tempo de início
#     try:
#         with open(caminho_arquivo, "r") as file:
#             conteudo = file.read()
#             print("Conteúdo do arquivo lido com sucesso.")
#     except FileNotFoundError:
#         print("Arquivo não encontrado.")
#     except Exception as e:
#         print(f"Ocorreu um erro ao ler o arquivo: {e}")
#     end_time = time.time()  # Registrar o tempo de fim
#     print(f"Tempo de leitura do arquivo: {end_time - start_time:.2f} segundos")


# # Função para calcular a soma de uma lista de números
# def calcular_soma(lista_numeros):
#     start_time = time.time()  # Registrar o tempo de início
#     soma = sum(lista_numeros)
#     end_time = time.time()  # Registrar o tempo de fim
#     print(f"A soma dos números é: {soma}")
#     print(f"Tempo de cálculo da soma: {end_time - start_time:.2f} segundos")


# def main(caminho_arquivo):
#     print("\n" + ("-" * 40))
#     print("Teste usando threads:")
#     # Definir a lista de números
#     lista_numeros = list(range(1, 100000001))  # Lista com números de 1 a 100.000.000

#     # Criar threads para as duas tarefas
#     thread_arquivo = threading.Thread(target=ler_arquivo, args=(caminho_arquivo,))
#     thread_soma = threading.Thread(target=calcular_soma, args=(lista_numeros,))

#     # Iniciar as threads
#     start_time = time.time()  # Tempo de início geral
#     thread_arquivo.start()
#     thread_soma.start()

#     # Esperar que ambas as threads terminem
#     thread_arquivo.join()
#     thread_soma.join()
#     end_time = time.time()  # Tempo de fim geral

#     print("Ambas as tarefas foram concluídas.")
#     print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")

#     print("\n" + ("-" * 40))
#     print("Teste de execução do modo tradicional")
#     start_time2 = time.time()
#     ler_arquivo(caminho_arquivo)
#     calcular_soma(lista_numeros)
#     end_time2 = time.time()
#     print(f"Tempo total de execução: {end_time2 - start_time2:.2f} segundos\n\n")

# Novo código, aparentemente funcionando:
from concurrent.futures import ThreadPoolExecutor


def ler_arquivo(caminho_arquivo):
    start_time = time.perf_counter()
    try:
        with open(caminho_arquivo, "r") as file:
            conteudo = file.read()
        return len(conteudo), time.perf_counter() - start_time
    except FileNotFoundError:
        return "Arquivo não encontrado", time.perf_counter() - start_time
    except Exception as e:
        return f"Erro: {e}", time.perf_counter() - start_time


def calcular_soma(lista_numeros):
    start_time = time.perf_counter()
    soma = sum(lista_numeros)
    return soma, time.perf_counter() - start_time


def executar_tarefas_em_paralelo(caminho_arquivo, lista_numeros):
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_arquivo = executor.submit(ler_arquivo, caminho_arquivo)
        future_soma = executor.submit(calcular_soma, lista_numeros)

        resultado_arquivo, tempo_arquivo = future_arquivo.result()
        resultado_soma, tempo_soma = future_soma.result()

    return (resultado_arquivo, tempo_arquivo), (resultado_soma, tempo_soma)


def executar_tarefas_sequencial(caminho_arquivo, lista_numeros):
    resultado_arquivo, tempo_arquivo = ler_arquivo(caminho_arquivo)
    resultado_soma, tempo_soma = calcular_soma(lista_numeros)
    return (resultado_arquivo, tempo_arquivo), (resultado_soma, tempo_soma)


def main(caminho_arquivo):
    lista_numeros = list(range(1, 100000001))

    print("\n" + ("-" * 40))
    print("Teste usando threads:")
    start_time = time.perf_counter()
    (resultado_arquivo, tempo_arquivo), (resultado_soma, tempo_soma) = (
        executar_tarefas_em_paralelo(caminho_arquivo, lista_numeros)
    )
    tempo_total = time.perf_counter() - start_time

    print(f"Resultado da leitura: {resultado_arquivo}")
    print(f"Tempo de leitura do arquivo: {tempo_arquivo:.4f} segundos")
    print(f"A soma dos números é: {resultado_soma}")
    print(f"Tempo de cálculo da soma: {tempo_soma:.4f} segundos")
    print(f"Tempo total de execução: {tempo_total:.4f} segundos")

    print("\n" + ("-" * 40))
    print("Teste de execução do modo tradicional")
    start_time = time.perf_counter()
    (resultado_arquivo, tempo_arquivo), (resultado_soma, tempo_soma) = (
        executar_tarefas_sequencial(caminho_arquivo, lista_numeros)
    )
    tempo_total = time.perf_counter() - start_time

    print(f"Resultado da leitura: {resultado_arquivo}")
    print(f"Tempo de leitura do arquivo: {tempo_arquivo:.4f} segundos")
    print(f"A soma dos números é: {resultado_soma}")
    print(f"Tempo de cálculo da soma: {tempo_soma:.4f} segundos")
    print(f"Tempo total de execução: {tempo_total:.4f} segundos")


main(caminho_arquivo)

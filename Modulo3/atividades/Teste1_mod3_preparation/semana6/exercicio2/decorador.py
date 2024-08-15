import time


def medir_tempo_execucao(func):
    """Decorador para medir o tempo de execução de uma função."""

    def wrapper(*args, **kwargs):
        inicio = time.time()  # Registra o tempo de início
        resultado = func(*args, **kwargs)  # Executa a função
        fim = time.time()  # Registra o tempo de fim
        tempo_execucao = fim - inicio  # Calcula o tempo total de execução
        print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
        return resultado

    return wrapper


@medir_tempo_execucao
def fibonacci(n):
    """Calcula o n-ésimo número de Fibonacci de forma recursiva."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Testando o decorador com a função fibonacci
print(fibonacci(15))  # A função fibonacci(30) pode demorar um tempo considerável


# Explicação:
# Importação:

# time é importado para medir o tempo.
# Decorador medir_tempo_execucao:

# Definição: Recebe uma função func como argumento.
# Wrapper: Função interna que mede o tempo de execução. Registra o tempo antes e depois da execução da função original (func). Calcula a diferença e imprime o tempo total.
# Retorno: O wrapper retorna o resultado da função original.
# Função fibonacci:

# Descrição: Calcula o n-ésimo número da sequência de Fibonacci de forma recursiva. Esta abordagem é lenta para valores maiores de n devido à sua complexidade exponencial.
# Aplicação do Decorador:

# O decorador é aplicado à função fibonacci usando o símbolo @.
# Quando você executa o código, o decorador medir_tempo_execucao irá imprimir o tempo de execução da função fibonacci além do resultado da função.

# Observações Adicionais:
# Desempenho: O cálculo recursivo da sequência de Fibonacci é ineficiente para valores grandes de n. Para cálculos mais rápidos, você pode considerar a implementação de versões iterativas ou usar memoização.
# Precisão: O tempo de execução é medido em segundos, e você pode ajustar a precisão no print (:.6f significa 6 casas decimais).
# Esse decorador pode ser usado com qualquer função para medir o tempo de execução, tornando-o uma ferramenta útil para otimização e análise de desempenho.

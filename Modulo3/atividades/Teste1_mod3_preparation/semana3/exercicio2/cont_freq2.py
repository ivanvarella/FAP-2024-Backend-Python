import string


def contar_frequencia_palavras(frase):
    # Remove pontuações e coloca a frase em minúsculas
    frase = frase.lower()
    frase = frase.translate(
        str.maketrans("", "", string.punctuation)
    )  # Remove pontuações
    palavras = frase.split()  # Divide a frase em palavras

    # Conta a frequência de cada palavra
    frequencias = {}
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1

    return frequencias


def main(frase_inicial):
    frequencias = contar_frequencia_palavras(frase_inicial)

    # Ordena as palavras pela frequência em ordem decrescente
    palavras_ordenadas = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)

    print("Palavras em ordem:", palavras_ordenadas)

    print("\nFrequência de cada palavra (ordenado por frequência):")
    for palavra, contagem in palavras_ordenadas:
        print(f"{palavra}: {contagem}")


# Texto de exemplo
frase_inicial = """A inteligência artificial (IA) é uma área fascinante da ciência da computação. A IA é a capacidade de uma máquina de imitar a inteligência humana. Com a IA, máquinas podem realizar tarefas que normalmente exigiriam inteligência humana, como entender linguagem natural, reconhecer padrões e tomar decisões. A IA é usada em muitos campos, desde assistência virtual até diagnóstico médico. A IA também está presente em sistemas de recomendação, como aqueles usados por serviços de streaming para sugerir filmes e músicas. As tecnologias de IA, como aprendizado de máquina e redes neurais, permitem que sistemas aprendam e se adaptem com base em dados. O aprendizado de máquina é um subcampo da IA que envolve treinar algoritmos para reconhecer padrões e fazer previsões. Redes neurais, inspiradas no funcionamento do cérebro humano, são usadas para resolver problemas complexos. A IA é uma tecnologia em rápida evolução, com novas descobertas e avanços ocorrendo constantemente. É importante estar atualizado sobre os desenvolvimentos em IA para entender como essas tecnologias podem impactar nosso futuro. A IA continuará a transformar a forma como vivemos e trabalhamos, trazendo novos desafios e oportunidades."""

# Executa o main
main(frase_inicial)


# Sintaxe sorted()
# # Sintaxe:
# sorted(iterable, key=None, reverse=False)

# # Argumentos:
# # - iterable: (Obrigatório) O iterável que você deseja ordenar. Pode ser uma lista, tupla, string, ou qualquer outro iterável.

# # - key: (Opcional) Uma função que serve como chave de ordenação. Cada elemento do iterável é passado para a função, e o valor retornado é usado para determinar a ordem. Por exemplo, key=str.lower poderia ser usado para ordenar strings de forma case-insensitive.

# # - reverse: (Opcional) Um valor booleano. Se True, a lista resultante será ordenada em ordem decrescente. O padrão é False (ordem crescente).

# # Exemplo 1: Ordenar uma lista de strings de forma case-insensitive:
# strings = ["Banana", "apple", "Cherry", "date"]
# ordenado = sorted(strings, key=str.lower)
# print(ordenado)  # Saída: ['apple', 'Banana', 'Cherry', 'date']

# # Exemplo 2: Ordenar uma lista de tuplas pelo segundo elemento de cada tupla: Usando a função Lambda
# tuplas = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
# ordenado = sorted(tuplas, key=lambda x: x[1])
# print(ordenado)  # Saída: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

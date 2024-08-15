frase_inicial = """A inteligência artificial (IA) é uma área fascinante da ciência da computação. A IA é a capacidade de uma máquina de imitar a inteligência humana. Com a IA, máquinas podem realizar tarefas que normalmente exigiriam inteligência humana, como entender linguagem natural, reconhecer padrões e tomar decisões. A IA é usada em muitos campos, desde assistência virtual até diagnóstico médico. A IA também está presente em sistemas de recomendação, como aqueles usados por serviços de streaming para sugerir filmes e músicas. As tecnologias de IA, como aprendizado de máquina e redes neurais, permitem que sistemas aprendam e se adaptem com base em dados. O aprendizado de máquina é um subcampo da IA que envolve treinar algoritmos para reconhecer padrões e fazer previsões. Redes neurais, inspiradas no funcionamento do cérebro humano, são usadas para resolver problemas complexos. A IA é uma tecnologia em rápida evolução, com novas descobertas e avanços ocorrendo constantemente. É importante estar atualizado sobre os desenvolvimentos em IA para entender como essas tecnologias podem impactar nosso futuro. A IA continuará a transformar a forma como vivemos e trabalhamos, trazendo novos desafios e oportunidades."""


from collections import Counter


def contar_frequencia_palavras(frase):
    # Remove pontuações e coloca a frase em minúsculas
    frase = frase.lower()
    palavras = frase.split()  # Divide a frase em palavras

    # Conta a frequência das palavras
    frequencias = Counter(palavras)

    return frequencias


def main(frase_inicial):
    frequencias = contar_frequencia_palavras(frase_inicial)

    print("\nFrequência de cada palavra:")
    for palavra, contagem in frequencias.items():
        print(f"{palavra}: {contagem}")


main(frase_inicial)

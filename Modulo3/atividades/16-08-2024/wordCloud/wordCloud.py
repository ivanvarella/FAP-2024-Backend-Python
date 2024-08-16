from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import nltk
from nltk.corpus import stopwords


caminho_projeto = os.path.join(
    os.getcwd(),
    "Modulo3",
    "atividades",
    "16-08-2024",
    "wordCloud",
)
caminho_arquivo = os.path.join(caminho_projeto, "texto.txt")

# print(caminho_arquivo)


with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    try:
        texto = arquivo.read()

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# for linha in texto.split("\n"):
#     print(linha)


def contar_palavras(texto):
    palavras = (
        texto.split()
    )  # Aqui está "pegando" até as pontuações, por isso dá um número maior
    frequencia = Counter(palavras)

    print(
        f"\n\n######################################################################################################"
    )
    print(f"         Dados do texto Sem remover as stopwords ")
    print(
        f"######################################################################################################"
    )
    print(f"Quantidade de palavras: {len(palavras)}")
    print(f"As 10 palavras mais frequentes: {frequencia.most_common(10)}")
    print(f"Quantidade de palavras únicas: {len(frequencia)}")
    print(
        f"######################################################################################################\n\n"
    )

    return frequencia


def gerar_nuvem_palavras(frequencia):
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(frequencia)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Contando a frequência das palavras na frase
frequencia_palavras = contar_palavras(texto)

# Gerando a nuvem de palavras
gerar_nuvem_palavras(frequencia_palavras)

# -----------------------------------------------------------------------------------------------------------------
# Removendo stopwords (palavras sem relevência para o entendimento do conteúdo do texto)

# Lista manual de stopwords em português
stop_words = set(
    [
        "o",
        "a",
        "e",
        "os",
        "as",
        "do",
        "da",
        "dos",
        "das",
        "de",
        "em",
        "um",
        "uma",
        "uns",
        "umas",
        "com",
        "por",
        "para",
        "no",
        "na",
        "nos",
        "nas",
        "ao",
        "à",
        "aos",
        "às",
        "que",
        "se",
        "é",
    ]
)


def remover_stopwords(texto):
    palavras = (
        texto.lower().split()
    )  # Converte para minúsculas e divide a frase em palavras - Remove todas as pontuações
    palavras_filtradas = [
        palavra
        for palavra in palavras
        if palavra.isalpha() and palavra not in stop_words
    ]
    return palavras_filtradas


def contar_palavras_stop_words(frase):
    palavras_filtradas = remover_stopwords(frase)
    frequencia = Counter(palavras_filtradas)

    print(
        f"\n\n######################################################################################################"
    )
    print(f"         Dados do texto Removendo as stopwords ")
    print(
        f"######################################################################################################"
    )
    print(f"Quantidade de palavras: {len(palavras_filtradas)}")
    print(f"As 10 palavras mais frequentes: {frequencia.most_common(10)}")
    print(f"Quantidade de palavras únicas: {len(frequencia)}")
    print(
        f"######################################################################################################\n\n"
    )

    return frequencia


def gerar_nuvem_palavras_stop_words(frequencia):
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(frequencia)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Contando a frequência das palavras na frase
frequencia_palavras = contar_palavras_stop_words(texto)

# Gerando a nuvem de palavras
gerar_nuvem_palavras_stop_words(frequencia_palavras)


# -----------------------------------------------------------------------------------------------------------------
# Removendo stopwords utilizando a lib NLTK que já contém uma lista de stopwords em cada idioma


def remover_stopwords_nltk(texto):
    stop_words = set(stopwords.words("portuguese"))
    palavras = nltk.word_tokenize(texto.lower())  # Tokeniza e converte para minúsculas
    palavras_filtradas = [
        palavra
        for palavra in palavras
        if palavra.isalpha() and palavra not in stop_words
    ]
    return palavras_filtradas


def contar_palavras_stop_words_nltk(texto):
    palavras_filtradas = remover_stopwords(texto)
    frequencia = Counter(palavras_filtradas)

    print(
        f"\n\n######################################################################################################"
    )
    print(f"         Dados do texto Removendo as stopwords - NLTK ")
    print(
        f"######################################################################################################"
    )
    print(f"Quantidade de palavras: {len(palavras_filtradas)}")
    print(f"As 10 palavras mais frequentes: {frequencia.most_common(10)}")
    print(f"Quantidade de palavras únicas: {len(frequencia)}")
    print(
        f"######################################################################################################\n\n"
    )

    return frequencia


def gerar_nuvem_palavras_stop_words_nltk(frequencia):
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(frequencia)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Contando a frequência das palavras na frase
frequencia_palavras = contar_palavras_stop_words_nltk(texto)

# Gerando a nuvem de palavras
gerar_nuvem_palavras_stop_words_nltk(frequencia_palavras)

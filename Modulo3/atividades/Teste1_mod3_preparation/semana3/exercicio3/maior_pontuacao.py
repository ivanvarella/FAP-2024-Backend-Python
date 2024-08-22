def encontrar_maior_pontuacao(lista_tuplas):
    # Usa a função max() com um lambda para obter a tupla com a maior pontuação
    tupla_max = max(lista_tuplas, key=lambda x: x[1])
    # Retorna o primeiro nome encontrado da pessoa com a maior pontuação
    # Se existir duas ou mais pessoas com a mesma potuação, irá retornar a primeira
    return tupla_max[0]


def main():
    # Lista de tuplas com nomes brasileiros engraçados e pontuações
    lista_tuplas = [
        ("Zé das Couves", 78),
        ("João da Silva", 85),
        ("Margarida Pimentel", 92),
        ("Tadeu Trombada", 55),
        ("Dona Neide", 88),
        ("Chico Bala", 90),
        ("Beto Carrero", 83),
        ("Joaquim Ninguém", 77),
        ("Mariana Sem Sotaque", 95),
        ("Cleusa Maluca", 98),
    ]

    # Encontra e exibe o nome da pessoa com a maior pontuação
    nome_maior_pontuacao = encontrar_maior_pontuacao(lista_tuplas)
    print(f"A pessoa com a maior pontuação é: {nome_maior_pontuacao}")


main()

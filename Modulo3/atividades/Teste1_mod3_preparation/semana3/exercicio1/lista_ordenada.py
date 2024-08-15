def obter_lista_usuario():
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista = entrada.split()  # Divide a string em uma lista de strings
    return lista


def processar_lista(lista):
    # Converte os itens da lista para float (ou int, se preferir)
    try:
        lista_numeros = [float(num) for num in lista]
    except ValueError:
        print("Entrada inválida. Certifique-se de que todos os itens sejam números.")
        return None

    # Remove duplicatas usando set e ordena a lista
    lista_unica = list(set(lista_numeros))
    # lista_unica.sort(reverse=True)  # Ordena em ordem decrescente
    lista_unica.sort()
    return lista_unica


def main():
    lista_usuario = obter_lista_usuario()
    lista_processada = processar_lista(lista_usuario)

    if lista_processada is not None:
        print(f"Lista ordenada sem duplicatas: {lista_processada}")


main()

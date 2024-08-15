def pega_lista_valores():
    lista = []
    while True:
        valor = input("Digite um número ou sair: ")

        if valor.lower() == "sair":
            # Dá o break e já retorna a lista
            return lista

        try:
            novo_numero = float(valor)  # Verifica se a entrada é um número
            lista.append(novo_numero)
        except ValueError:
            print("Entrada inválida.")
            # Volta para o início do loop
            continue


def soma_pares(lista):
    lista_pares = []
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
            lista_pares.append(numero)
    return soma, lista_pares


def main():
    lista_numeros = pega_lista_valores()
    print(f"\n\n\nLista dos números: {lista_numeros}. \n\n")

    resultado_soma_pares, lista_pares = soma_pares(lista_numeros)

    print(f"Lista dos números pares: {lista_pares}. \n\n")
    print(f"Soma dos números pares: {resultado_soma_pares}\n\n")


main()

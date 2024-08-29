from functools import reduce

lista = [100, 200, 50, 120, 400]

resultado = reduce(lambda arg1, arg2: arg1 + arg2, lista) / len(lista)
print(resultado)

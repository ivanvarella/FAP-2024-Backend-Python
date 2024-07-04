# 9. Intercalador de Listas: Crie uma função que receba duas listas de 10 elementos
# cada e gere uma terceira lista de 20 elementos, cujos valores sejam compostos
# pelos elementos intercalados das duas outras listas.

#import random

def misturaListas(lista1, lista2):
  lista3 = []
  for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
  #random.shuffle(lista3)
  return lista3


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["carro", "python", "árvore", "livro", "computador", "gato", "cachorro", "música", "cidade", "oceano"]

lista3 = misturaListas(lista1, lista2)

print(f"Elementos da primeira lista: {lista1}")
print(f"Elementos da segunda lista: {lista2}")
print(f"Elementos intercalados: {lista3}")
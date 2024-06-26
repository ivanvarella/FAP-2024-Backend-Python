# geração de valores aleatórios

import random

# seed

# random - 0 e 1
numero_aleatorio = random.random()
print(numero_aleatorio)

# randrange (exclusivo) e randint (inclusivo)
numero_0a100 = random.randint(0, 5)
print(numero_0a100)

# choice e choices (pode pegar itens repetidos)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(random.choices(numeros, k=2))

# sample (sempre itens diferentes)
print(random.sample(numeros, k=2))

# shuffle
print(numeros)
random.shuffle(numeros)
print(numeros)

# variantes (gauss, normalvariate, etc.)
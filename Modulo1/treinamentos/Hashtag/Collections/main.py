# objetivo - estruturas auxiliares às estruturas padrões do Python


# counter
from collections import Counter

estoque = ["iphone", "iphone", "ipad", "airpod", "ipad", "iphone", "iphone", "airpod", "macbook"]

dic_counter = Counter(estoque)
print(dic_counter)
print(dic_counter["iphone"])


# default dict
from collections import defaultdict

vendas = {"André": 1000, "João": 2000, "Lira": 500, "Amanda": 1500, "Carol": 3000, "Marcus": 200, "Camila": 400, "Andreia": 8000}
meta1 = 1000
meta2 = 2000

dic_bonus = defaultdict(list)

for vendedor in vendas:
    valor_vendas = vendas[vendedor]
    if valor_vendas > meta2:
        dic_bonus["meta2"].append(vendedor)
    elif valor_vendas > meta1:
        dic_bonus["meta1"].append(vendedor)
    else:
        dic_bonus["sem meta"].append(vendedor)

print(dic_bonus)

# ChainMap
brinquedos = {'Lego': 30, 'Banco Imobiliário': 10}
informatica = {'Tablet': 5, 'Mouse': 30, 'Iphone': 15}
roupas = {'Jeans': 150, 'Camisa': 100}

from collections import ChainMap

estoque = ChainMap(brinquedos, informatica, roupas)
print(estoque)
print(estoque["Tablet"])
print(list(estoque.keys()))

# deque
from collections import deque

fila = deque(["item1", "item2", "item3"])

fila.append("item4")
print(fila)
fila.appendleft("item5")
print(fila)

fila.pop()
print(fila)
fila.popleft()
print(fila)

# namedtuple
from collections import namedtuple

Produto = namedtuple("Produto", ["nome", "preco", "tamanho"])

produto1 = Produto("camisa", 150, "M")

print(produto1.nome)
print(produto1[0])
print(produto1.preco)

# OrderedDict - não mais necessário
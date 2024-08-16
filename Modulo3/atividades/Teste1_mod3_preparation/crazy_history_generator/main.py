import random

# Conjuntos de palavras pré-definidos
conjuntos_palavras = [
    {
        "nomes": [
            "Zé Bonitinho",
            "Chico Bento",
            "Dona Florinda",
            "Jeca Tatu",
            "Tia Anastácia",
            "Seu Madruga",
        ],
        "verbos": [
            "sambou",
            "fofocou",
            "tuitou",
            "atropelou",
            "dançou quadrilha",
            "engasgou",
        ],
        "adjetivos": [
            "hilário",
            "esquisito",
            "desengonçado",
            "absurdo",
            "inesquecível",
            "bizarro",
        ],
        "lugares": [
            "na feira",
            "no boteco",
            "no churrasco",
            "na laje",
            "no salão de beleza",
            "na quitanda",
        ],
    },
    {
        "nomes": [
            "Nega Maluca",
            "Zé Carioca",
            "Pedrinho",
            "Narizinho",
            "Candinho",
            "Sinhá Moça",
        ],
        "verbos": [
            "tacou fogo",
            "caiu do cavalo",
            "inventou moda",
            "contou vantagem",
            "se perdeu",
            "subiu no coqueiro",
        ],
        "adjetivos": [
            "fenomenal",
            "vergonhoso",
            "sem noção",
            "maluco",
            "desastroso",
            "hilário",
        ],
        "lugares": [
            "no morro",
            "na praia",
            "no sítio",
            "no carnaval",
            "na rua de baixo",
            "na beira do rio",
        ],
    },
    {
        "nomes": [
            "Seu Creysson",
            "Tião Macalé",
            "Dona Clotilde",
            "Compadre Washington",
            "Marieta Severo",
            "Cabo Daciolo",
        ],
        "verbos": [
            "levou o farelo",
            "bateu perna",
            "se escafedeu",
            "subiu no pau de sebo",
            "fez macumba",
            "quebrou tudo",
        ],
        "adjetivos": [
            "fuleiro",
            "retado",
            "danado",
            "cabuloso",
            "rocambolesco",
            "xexelento",
        ],
        "lugares": [
            "no terreiro",
            "no quintal",
            "na roça",
            "no forró",
            "no brejo",
            "no barraco",
        ],
    },
    {
        "nomes": [
            "Tonho da Lua",
            "Mãe Dináh",
            "Nega Juju",
            "Tião Galinha",
            "Cumpadi Tonho",
            "Sinhozinho Malta",
        ],
        "verbos": [
            "bateu uma laje",
            "fofocou no portão",
            "fez um corre",
            "fez um barraco",
            "comeu um pastel",
            "foi parar no xilindró",
        ],
        "adjetivos": [
            "doido de pedra",
            "cascudo",
            "estribado",
            "rebolado",
            "chave de cadeia",
            "bicho solto",
        ],
        "lugares": [
            "na casa da mãe Joana",
            "no puxadinho",
            "na biqueira",
            "na boca do lixo",
            "na feira de São Cristóvão",
            "no sambódromo",
        ],
    },
]


frases_de_efeito = [
    "Todo mundo que estava lá não pôde deixar de rir!",
    "E assim, um dia comum se tornou inesquecível!",
    "Ninguém acreditaria se não tivesse visto!",
    "A plateia ficou boquiaberta com o que aconteceu!",
    "Foi um momento que ninguém jamais esquecerá!",
    "E assim, todos tiveram uma história para contar!",
    "O que aconteceu depois deixou todos chocados!",
    "A surpresa foi tanta que ninguém sabia como reagir!",
    "E desde então, aquele dia virou lenda!",
    "Foi tão inesperado que virou o assunto do mês!",
]

inicio_frase = [
    "Certa vez",
    "Em um belo dia",
    "Num dia de chuva",
    "No meio de uma noite estrelada",
    "Numa tarde ensolarada",
    "Em um mundo distante",
    "No fundo de uma floresta encantada",
    "Em uma pequena cidade",
    "No topo de uma montanha",
    "Em um lugar misterioso",
    "Nas profundezas do oceano",
    "Na ponta de um arco-íris",
    "Em um reino mágico",
    "Durante uma tempestade",
    "No silêncio da madrugada",
    "Em uma aventura inesperada",
    "Na beira do abism,",
    "Numa estrada deserta",
    "No coração da selva",
    "Em um castelo antigo",
]


numero_paragrafos = 3

historia = []

for _ in range(numero_paragrafos):

    # Seleciona um conjunto aleatório de palavras
    conjunto_escolhido = random.choice(conjuntos_palavras)

    # Seleciona uma palavra aleatória de cada categoria
    nome_escolhido = random.choice(conjunto_escolhido["nomes"])
    verbo_escolhido = random.choice(conjunto_escolhido["verbos"])
    adjetivo_escolhido = random.choice(conjunto_escolhido["adjetivos"])
    lugar_escolhido = random.choice(conjunto_escolhido["lugares"])

    # Gera a história
    historia.append(
        f"{random.choice(inicio_frase)}, {nome_escolhido} {verbo_escolhido} "
        f"{adjetivo_escolhido} {lugar_escolhido}. \n"
        f"{random.choice(frases_de_efeito)} \n"
    )

# Exibe a história gerada
for parte in historia:
    print(parte)

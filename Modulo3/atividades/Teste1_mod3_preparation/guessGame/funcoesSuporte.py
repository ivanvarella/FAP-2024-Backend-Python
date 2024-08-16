import json
import os
from datetime import datetime
from random import randint
import time

# Para debugg - Está salvando duplicado no Json
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Caminho do diretório atual
caminho_projeto = os.path.join(
    os.getcwd(),
    "Modulo3",
    "atividades",
    "Teste1_mod3_preparation",
    "guessGame",
)
caminho = os.path.join(caminho_projeto, "recordes.json")

# print(caminho)


# Função para exibir o menu do jogo
def exibirMenu():
    codUser = None
    print("Jogo Guess the number\n")

    while True:
        print("###### Selecione uma opção ######")
        print("# Cod[1]: Mostrar recordes      #")
        print("# Cod[2]: Iniciar jogo          #")
        print("# Cod[3]: Sair                  #")
        print("# Cod[4]: About                 #")
        print("#################################\n")

        codUser = input("Digite o código:")

        if codUser == "4":
            print(
                "\nApesar de já estar funcional, os seguintes pontos estão pendentes e em andamento:"
            )
            print(
                "1 - Função para gravar recordes Json - atenção para o formato da data e de tempo (caso decida inserir também)"
            )
            print(
                "2 - Formulário com os dados do usuário para gravar no Json - Opção para gravar ou não"
            )
            print(
                "3 - Melhorar a lógica do jogo quando está aproximando do valor a ser encontrado\n"
            )
            break
        if codUser == "3":
            print("\nObrigado por jogar!\n\n")
            break
        elif codUser == "1":
            mostraRecordes()
            # Após mostrar os recordes, continua para o próximo loop do menu
        elif codUser == "2":
            iniciarJogo()
        else:
            print("\nOpção inválida!\n\n")


def iniciarJogo():
    print("\n-----------------------------------------------")
    print("Computador gerando um número aleatório.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    n1 = randint(1, 10)
    print("Número gerado com sucesso!\n")
    inicioContagemTempo = datetime.now()
    guess = int(input("Adivinhe qual foi o número:"))
    tentativas = 1

    if guess == n1:
        fimContagemTempo = datetime.now()
        horas, minutos, segundos = calculaTempoDecorrido(
            fimContagemTempo - inicioContagemTempo
        )
        print("Parabéns, você acertou!")
        print(
            f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {horas} horas, {minutos} minutos e {segundos} segundos!\n\n"
        )
        # Dados para adicionar o novo recorde à lista de recordes
        # Se acertou de primeira
        nome_player = input('Digite seu nome para adicionar aos recordes ou "sair": ')

        if nome_player.lower() != "sair":
            novoRecorde = obter_dados_recordes(
                nome_player, tentativas, horas, minutos, segundos
            )
            adicionaRecorde(novoRecorde)
            return
    else:
        while guess != n1:
            if guess < n1:
                print("Errou, o número é maior!")
            else:
                print("Errou, o número é menor!")
            tentativas += 1
            guess = int(input("Tente novamente:"))
        fimContagemTempo = datetime.now()
        horas, minutos, segundos = calculaTempoDecorrido(
            fimContagemTempo - inicioContagemTempo
        )
        print(
            f"Parabéns você acertou, o número gerado era o {n1}. Você só precisou de {tentativas} tentativas e terminou em {horas} horas, {minutos} minutos e {segundos} segundos!\n\n"
        )
        # Se não aceertou de primeira
        nome_player = input('Digite seu nome para adicionar aos recordes ou "sair": ')

        if nome_player.lower() != "sair":
            novoRecorde = obter_dados_recordes(
                nome_player, tentativas, horas, minutos, segundos
            )
            adicionaRecorde(novoRecorde)
            return


# Função para calcular o tempo decorrido até o jogar acertar
def calculaTempoDecorrido(difTempo):
    segundosTotal = difTempo.total_seconds()

    horas = segundosTotal // 3600
    minutos = (segundosTotal % 3600) // 60
    segundos = (segundosTotal % 3600) % 60

    horas = int(horas)
    minutos = int(minutos)
    segundos = round(segundos, 2)

    return horas, minutos, segundos


# Funcao para tratar o tempo do método datetime
def trataDataTime(dataHora):
    # Formatar a data no formato dd/mm/aaaa
    data = dataHora.strftime("%d/%m/%Y")

    # Formatar a hora no formato hh:mm
    hora = dataHora.strftime("%H:%M")

    return data, hora


# Função para mostrar os recordes
def mostraRecordes():
    with open(caminho, "r", encoding="utf-8") as file:
        recordes = json.load(file)
    print("\n\n######################")
    print("###### Recordes ######")
    print("######################\n")
    for recorde in recordes["Recordes"]:
        nome = recorde["nome"]
        tentativas = recorde["tentativas"]
        tempo = recorde["tempo"]
        data_recorde = recorde["data"]
        hora_recorde = recorde["hora"]
        print(f"Nome: {nome}")
        print(f"Tentativas: {tentativas}")
        print(f"Tempo: {tempo}")
        print(f"Data: {data_recorde}")
        print(f"Hora: {hora_recorde}")
        print("-----------------------------\n\n")


def obter_dados_recordes(nome_player, tentativas, horas, minutos, segundos):
    # Formatar a data e a hora
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    hora_formatada = agora.strftime("%H:%M")

    # Calcular o tempo total decorrido
    if horas == 0 and minutos == 0:
        tempo_partida = f"{segundos} segundos"
    elif horas == 0:
        tempo_partida = f"{minutos} minutos e {segundos} segundos"
    else:
        tempo_partida = f"{horas} horas, {minutos} minutos e {segundos} segundos"

    novoRecorde = {
        "nome": nome_player,
        "tentativas": tentativas,
        "tempo": tempo_partida,
        "data": data_formatada,
        "hora": hora_formatada,
    }
    return novoRecorde


# # Função para gravar novo recorde
# def adicionaRecorde(novoRecorde):

#     logging.debug("Iniciando função adicionaRecorde...")
#     # Carregar dados do arquivo JSON
#     with open(caminho, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     # Se o campo 'Recordes' não existir, inicializa-o como uma lista vazia
#     if "Recordes" not in data:
#         data["Recordes"] = []

#     # Adiciona o novo recorde à lista de recordes
#     data["Recordes"].append(novoRecorde)

#     print(f"Data antes de adicionar: {data}")

#     # Escrever de volta no arquivo JSON
#     with open(caminho, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

#         # Forçar a escrita imediata dos dados para o arquivo
#         # f.flush()
#     logging.debug("Registro adicionado com sucesso.")


def adicionaRecorde(novoRecorde):

    # logging.debug("Iniciando função adicionaRecorde...")
    # Carregar dados do arquivo JSON
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        # logging.error("Arquivo JSON não encontrado.")
        data = {"Recordes": []}
    except json.JSONDecodeError:
        # logging.error("Erro ao decodificar o JSON.")
        data = {"Recordes": []}

    # Se o campo 'Recordes' não existir, inicializa-o como uma lista vazia
    if "Recordes" not in data:
        data["Recordes"] = []

    # Adiciona o novo recorde à lista de recordes
    data["Recordes"].append(novoRecorde)

    # Verifique o conteúdo antes de gravar
    # print(f"Data antes de gravar: {data}")

    # Escrever de volta no arquivo JSON
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.flush()  # Forçar a escrita imediata dos dados
        # logging.debug("Registro adicionado com sucesso.")
    except IOError as e:
        logging.error(f"Erro ao escrever no arquivo JSON: {e}")


# Teste da função
# novoRecorde = {
#     "nome": "Teste",
#     "tentativas": 1,
#     "tempo": "00:00:01",
#     "data": "16/08/2024",
#     "hora": "12:00",
# }

# adicionaRecorde(novoRecorde)

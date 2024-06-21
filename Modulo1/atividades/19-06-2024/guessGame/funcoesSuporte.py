import json
import os
import jogo

# Para debugg - Está salvando duplicado no Json
import logging
# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Caminho do diretório atual
caminho = os.getcwd() + "/Modulo1/atividades/19-06-2024/guessGame/recordes.json"

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
        print("\nApesar de já estar funcional, os seguintes pontos estão pendentes e em andamento:")
        print("1 - Função para gravar recordes Json - atenção para o formato da data e de tempo (caso decida inserir também)")
        print("2- Formulário com os dados do usuário para gravar no Json - Opção para gravar ou não")
        print("2 - Função para ler recordes Json e exibir - Ok")
        print("3 - Melhorar a lógica do jogo quando está aproximando do valor a ser encontrado\n")
        break
    if codUser == "3":
        print("\nObrigado por jogar!\n\n")
        break
    elif codUser == "1":
        mostraRecordes()
        # Após mostrar os recordes, continua para o próximo loop do menu
    elif codUser == "2":
        jogo.iniciarJogo()
    else:
        print("\nOpção inválida!\n\n")

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
    with open(caminho, "r", encoding='utf-8') as file:
      recordes = json.load(file)
    print("\n\n######################")
    print("###### Recordes ######")
    print("######################\n")
    for recorde in recordes['Recordes']:
      nome = recorde['nome']
      tentativas = recorde['tentativas']
      tempo = recorde['tempo']
      data_recorde = recorde['data']
      hora_recorde = recorde['hora']
      print(f"Nome: {nome}")
      print(f"Tentativas: {tentativas}")
      print(f"Tempo: {tempo}")
      print(f"Data: {data_recorde}")
      print(f"Hora: {hora_recorde}")
      print("-----------------------------\n\n")

# Função para gravar novo recorde
def adicionaRecorde(novoRecorde):
  logging.debug('Iniciando função adicionaRecorde...')
  # Carregar dados do arquivo JSON
  with open(caminho, 'r', encoding='utf-8') as f:
    data = json.load(f)

  # Se o campo 'Recordes' não existir, inicializa-o como uma lista vazia
  if 'Recordes' not in data:
    data['Recordes'] = []

  # Adicionar novo recorde à lista de recordes
  data['Recordes'].append(novoRecorde)

  # Escrever de volta no arquivo JSON
  with open(caminho, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

    # Forçar a escrita imediata dos dados para o arquivo
    #f.flush()
  logging.debug('Registro adicionado com sucesso.')








# Teste Json:
#mostraRecordes()

#data, hora = trataDataTime(datetime.now())

#print(f"Data: {data} - Hora: {hora}")

# Teste add recorde:
novoRecorde = {
    "nome": "Nome Jogar teste",
    "tentativas": 400,
    "tempo": "05:15:37",
    "data": "18-06-2024",
    "hora": "15:30"
}

#adicionaRecorde(novoRecorde)
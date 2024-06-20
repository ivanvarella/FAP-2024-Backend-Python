##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####


import funcoesDeposito


print("\n++++  Cálculo da capacidade de um depósito  ++++\n\n")

# Entrada dados do depósito
# Altura
depositoAltura, erroTipoAlturaDep, erroVazioAlturaDep, erroMsgAlturaDep = funcoesDeposito.isValidInput("Digite a altura do depósito (m): ", "float")

# Largura
depositoLargura, erroTipoLarguraDep, erroVazioLarguraDep, erroMsgLarguraDep = funcoesDeposito.isValidInput("Digite a largura do depósito (m): ", "float")

# Profundidade
depositoProfundidade, erroTipoProfundidadeDep, erroVazioProfundidadeDep, erroMsgProfundidadeDep = funcoesDeposito.isValidInput("Digite a profundidade do depósito (m): ", "float")

# Cáculo volume depósito
depositoVolume = funcoesDeposito.calcVolumeDeposito(depositoAltura, depositoLargura, depositoProfundidade)

print("\n______________________________________________________")
print(f"\nO volume do depósito desejado é de {depositoVolume} m³.")
print("______________________________________________________\n")


# Carregar o JSON em um objeto Python
dadosBolas = funcoesDeposito.carregaDadosJson('bolas.json')

# Exibe as bolas pré-cadastradas no Json
print("Bolas cadastradas: ")
if 'Bolas' in dadosBolas:
    bolas = dadosBolas['Bolas']
    for indice, bola in enumerate(bolas):
        nomePrint = bola['nome']
        diametroPrint = bola['diametro']
        raioPrint = diametroPrint / 2
        print(f"[Cod.: {indice+1}] {nomePrint} - Diâmetro: {diametroPrint}cm - Volume: {round(funcoesDeposito.calcVolumeBola(raioPrint),2)}cm³")
else:
    print("Chave 'Bolas' não encontrada no JSON")

# Seleção da bola pré-cadastrada no Json ou adiciona uma nova bola ao Json (será usada para o cáculo)
bolaSelec = input("\nDigite o código da bola ou digite -1 para inserir outra bola: ")

# Cadastra nova bola no Json
if int(bolaSelec) == -1:
  novoNome = input("Digite o nome da bola: ")
  while True:
    novoDiametro = input("Digite o diâmetro da bola(cm): ")
    if novoDiametro == "":
      print("O campo não pode ser vazio!")
    else:
      novoDiametro = float(novoDiametro)
      round(novoDiametro, 2)
      isValid = funcoesDeposito.isValid(novoDiametro, "intFloat")
      if isValid:
        break
      else:
        print("O campo deve ser um valor numérico!")
        continue
  # Cadastra a nova bola no JSON
  funcoesDeposito.cadastrarBola(novoNome, novoDiametro)
  raio = novoDiametro / 2
  volumeBola = round(funcoesDeposito.calcVolumeBola(raio), 2)
  # Calcular o número máximo de bolas que cabem, exibir o resultado e finalizar o programa
  numMaxBolasDeposito = funcoesDeposito.calcMaxBolas(novoDiametro, depositoVolume)
  print("\n--------------------------------------------------- Resultado ---------------------------------------------------")
  print(f"\nO máximo de bolas ({novoNome} - Diâmetro: {novoDiametro}cm - Volume: {volumeBola}cm³) que cabem no depósito ({depositoVolume}m³) é de {int(numMaxBolasDeposito)} bolas.\n")
  print("-----------------------------------------------------------------------------------------------------------------\n\n")
# Usa a bola pré-cadastrada
else:
    while True:
      indiceBola = int(bolaSelec) - 1
      if (indiceBola >= 0) and (indiceBola < len(bolas)):
          nome = bolas[indiceBola]['nome']
          diametro = bolas[indiceBola]['diametro']
          raio = diametro / 2
          volumeBola = round(funcoesDeposito.calcVolumeBola(raio), 2)
          print(f"\nBola selecionada: {nome} - Diâmetro: {diametro}cm - Volume: {volumeBola}cm³")
          # Calcular o número máximo de bolas que cabem, exibir o resultado e finalizar o programa
          numMaxBolasDeposito = funcoesDeposito.calcMaxBolas(diametro, depositoVolume)
          print("\n--------------------------------------------------- Resultado ---------------------------------------------------")
          print(f"\nO máximo de bolas ({nome} - Diâmetro: {diametro}cm - Volume: {volumeBola}cm³) que cabem no depósito ({depositoVolume}m³) é de {int(numMaxBolasDeposito)} bolas.\n")
          print("-----------------------------------------------------------------------------------------------------------------\n\n")
          break
      else:
          print("Código inválido")
          bolaSelec = input("Digite o código da bola: ")

print("\n++++  FIM DO PROGRAMA  ++++\n")
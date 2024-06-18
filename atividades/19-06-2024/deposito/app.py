##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####


import funcoesDeposito


print("\n++++  Cálculo da capacidade de um depósito  ++++\n\n")

# Entrada dados do depósito
depositoAltura = float(input("Digite a altura do depósito (m): "))
depositoLargura = float(input("Digite a largura do depósito (m): "))
depositoProfundidade = float(input("Digite a profundidade do depósito (m): "))

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
    novoDiametro = float(input("Digite o diâmetro da bola(cm): "))
    novoDiametro = round(novoDiametro, 2)
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



'''
## Falta:
1- Função calcular o máximo de bolas que cabem no depósito - Ok
2- Exição das informações: máximo de bolas que cabem, dados do depósito e da bola escolhida ou armazenada no Json - Ok
3- Validação dos dados inseridos (ex: diâmetro, etc), tentar usar funções de validação para separar o código deixando mais limpo e fácil de entender
4- Teste do programa

Bolas cadastradas: 
[Cod.: 1] Bola de Basquete Adulto - Diâmetro: 24cm - Volume: 7238.23cm³
[Cod.: 2] Bola de Basquete Infantil - Diâmetro: 22cm - Volume: 5575.28cm³
[Cod.: 3] Bola de Futebol Oficial - Diâmetro: 22cm - Volume: 5575.28cm³
[Cod.: 4] Bola de Vôlei - Diâmetro: 21cm - Volume: 4849.05cm³
[Cod.: 5] Bola de Handball - Diâmetro: 19cm - Volume: 3591.36cm³
[Cod.: 6] Bola de Futebol de Salão - Diâmetro: 20cm - Volume: 4188.79cm³
[Cod.: 7] Bola de fogo - Diâmetro: 300.0cm - Volume: 14137166.94cm³
[Cod.: 8] Bola de boliche - Diâmetro: 38.0cm - Volume: 28730.91cm³

altura = diametro
Raio = diametro / 2
VolumeEsfera = 4/3 * pi * raio ** 3
Circunferencia  = 2 * pi * raio
'''
##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####


print("++++  Cálculo de IMC!  ++++")

def imcCalc(peso, altura):
  return round((peso / altura ** 2), 2)

def imcClassificacao(imc):
  if imc < 18.5:
    return "Abaixo do peso"
  elif imc >= 18.5 and imc < 25:
    return "Peso normal"
  elif imc >= 25 and imc < 30:
    return "Sobrepeso"
  elif imc >= 30 and imc < 35:
    return "Obesidade Grau I"
  elif imc >= 35 and imc < 40:
    return "Obesidade Grau II"
  elif imc >= 40:
    return "Obesidade Grau III ou Mórbida"

while True:
  altura = float(input("Digite a altura(m) ou -1 para sair: "))
  if altura == -1:
      print("++++  Fim do programa  ++++")
      break
  elif altura <= 0.6 or altura >= 2.5:
      print("Altura inválida!")
  else:
      while True:
          peso = float(input("Digite o peso(kg) ou -1 para sair: "))
          if peso == -1:
              print("++++  Fim do programa  ++++")
              break
          elif peso <= 15 or peso >= 250:
              print("Peso inválido!")
          else:
              imc = imcCalc(peso, altura)
              classificacao = imcClassificacao(imc)
              print(f"IMC: {imc} - {classificacao}")
              print("++++  Fim do programa  ++++")
              break
      break

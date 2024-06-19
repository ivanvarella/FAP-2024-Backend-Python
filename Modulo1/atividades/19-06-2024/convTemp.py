##### FAP Backend Python - Turma 17 ####
##### Ivan Varella ####
##### Pedro Vinícius ####

print("Conversor de temperatura/n/n")
print("[Cod. 1] Celsius para Fahrenheit")
print("[Cod. 2] Fahrenheit para Celsius")


escala = input("Qual escala de temperatura deseja converter utilizando os códigos acima: ")



temp1 = float(input("Digite a temperatura: "))

if escala == "1":
    temp2 = (temp1 * 9/5) + 32
    print(f"A conversão da temperatura {temp1}C para a escala de Fahrenheit é: {temp2} F")
elif escala == "2":
    temp2 = (temp1 - 32) * 5/9
    print(f"A conversão da temperatura {temp1}F para a escala de Celsius é: {temp2} C")
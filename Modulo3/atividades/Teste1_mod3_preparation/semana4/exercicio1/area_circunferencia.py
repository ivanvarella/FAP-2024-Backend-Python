import math

try:
    raio = float(input("Digite o raio do círculo: "))
    if raio < 0:
        print("O raio não pode ser negativo.")
    else:
        area = math.pi * raio**2
        circunferencia = 2 * math.pi * raio

        print(f"A área do círculo é: {area:.2f}")
        print(f"A circunferência do círculo é: {circunferencia:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")

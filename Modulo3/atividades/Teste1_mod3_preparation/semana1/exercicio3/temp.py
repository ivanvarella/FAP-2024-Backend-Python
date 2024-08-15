def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin."""
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius."""
    return kelvin - 273.15


def fahrenheit_para_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin."""
    # Primeiro, converte Fahrenheit para Celsius
    celsius = fahrenheit_para_celsius(fahrenheit)
    # Em seguida, converte Celsius para Kelvin
    return celsius_para_kelvin(celsius)


def kelvin_para_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit."""
    # Primeiro, converte Kelvin para Celsius
    celsius = kelvin_para_celsius(kelvin)
    # Em seguida, converte Celsius para Fahrenheit
    return celsius_para_fahrenheit(celsius)


def main():
    while True:
        # Solicita a temperatura ao usuário
        temperatura = input("Digite a temperatura (ou 'sair' para encerrar): ")

        if temperatura.lower() == "sair":
            break

        try:
            temperatura = float(temperatura)
        except ValueError:
            print("Por favor, insira um valor numérico para a temperatura.")
            # Volta para o início do loop while e solicita novamente a temperatura
            continue

        # Solicita ao usuário a direção da conversão
        direcao = input(
            "Escolha a direção da conversão (1: Celsius para Fahrenheit, 2: Fahrenheit para Celsius, "
            "3: Celsius para Kelvin, 4: Kelvin para Celsius, "
            "5: Fahrenheit para Kelvin, 6: Kelvin para Fahrenheit) ou sair: "
        )

        if direcao == "1":
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}°F")
        elif direcao == "2":
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura}°F é igual a {resultado:.2f}°C")
        elif direcao == "3":
            resultado = celsius_para_kelvin(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}K")
        elif direcao == "4":
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura}K é igual a {resultado:.2f}°C")
        elif direcao == "5":
            resultado = fahrenheit_para_kelvin(temperatura)
            print(f"{temperatura}°F é igual a {resultado:.2f}K")
        elif direcao == "6":
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura}K é igual a {resultado:.2f}°F")
        elif direcao.lower() == "sair":
            break
        else:
            print(
                "Direção de conversão inválida. Por favor, escolha um número entre 1 e 6."
            )


main()

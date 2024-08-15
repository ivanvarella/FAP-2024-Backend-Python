class Carro:
    def __init__(self, marca, modelo, ano):
        """
        Inicializa um novo objeto Carro com a marca, modelo e ano fornecidos.

        :param marca: Marca do carro
        :param modelo: Modelo do carro
        :param ano: Ano de fabricação do carro
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar_carro(self):
        """
        Imprime uma mensagem indicando que o carro está sendo ligado.
        """
        print(f"Ligando o {self.modelo}...")

    def desligar_carro(self):
        """
        Imprime uma mensagem indicando que o carro está sendo desligado.
        """
        print(f"Desligando o {self.modelo}...")

    def __str__(self) -> str:
        """
        Retorna uma representação em string do carro.

        :return: Uma string formatada com a marca, modelo e ano do carro
        """
        return f"{self.marca} - {self.modelo} ({self.ano})"


def main():
    # Criação de vários objetos Carro
    carro1 = Carro("Fiat", "Uno", 2010)
    carro2 = Carro("Volkswagen", "Gol", 2015)
    carro3 = Carro("Chevrolet", "Onix", 2020)
    carro4 = Carro("Ford", "Ka", 2018)
    carro5 = Carro("Toyota", "Corolla", 2022)

    # Lista de carros para iteração
    carros = [carro1, carro2, carro3, carro4, carro5]

    # Demonstração do uso dos métodos ligar_carro, desligar_carro e __str__
    for carro in carros:
        print(carro)  # Exibe a representação em string do carro
        carro.ligar_carro()  # Liga o carro
        carro.desligar_carro()  # Desliga o carro
        print("-" * 40)


main()

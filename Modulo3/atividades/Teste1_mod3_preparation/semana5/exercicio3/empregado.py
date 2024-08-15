from pessoa import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome, idade, salario=None, cargo=None):
        super().__init__(nome, idade)
        self.salario = salario
        self.cargo = cargo
        self.status = "ativo" if cargo and salario else "desempregado"

    def __str__(self):
        if self.status == "ativo":
            return f"{self.nome} tem {self.idade} anos, é um empregado com salário de R${self.salario} e está trabalhando como {self.cargo}."
        else:
            return f"{self.nome} tem {self.idade} anos, não está empregado."

    def trabalhar(self):
        if self.status == "ativo":
            print(f"{self.nome} está trabalhando.")
        else:
            print(f"{self.nome} não pode trabalhar porque está desempregado.")

    def receber_salario(self):
        if self.status == "ativo":
            print(f"{self.nome} recebeu o salário de R${self.salario}.")
        else:
            print(f"{self.nome} não pode receber salário porque está desempregado.")

    def contratar(self, novo_cargo, novo_salario):
        if self.status == "ativo":
            print(f"{self.nome} já está empregado, promovendo...")
            self.promover(novo_cargo, novo_salario)
        else:
            print(f"{self.nome} foi contratado para o cargo de {novo_cargo}.")
            self.cargo = novo_cargo
            self.salario = novo_salario
            self.status = "ativo"

    def demitir(self):
        if self.status == "ativo":
            print(f"Demitindo {self.nome} do cargo de {self.cargo}...")
            self.status = "desempregado"
            self.cargo = None
            self.salario = None
            print(f"{self.nome} foi demitido.")
        else:
            print(f"{self.nome} já está desempregado.")

    def promover(self, novo_cargo, novo_salario):
        if self.status == "ativo":
            print(f"{self.nome} foi promovido para o cargo de {novo_cargo}.")
            self.cargo = novo_cargo
            self.salario = novo_salario
        else:
            print(f"{self.nome} não pode ser promovido porque está desempregado.")

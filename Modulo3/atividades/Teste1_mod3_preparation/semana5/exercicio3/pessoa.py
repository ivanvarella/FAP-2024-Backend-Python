class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

    def __repr__(self):
        return f"<Pessoa: {self.nome} ({self.idade})>"

# Classe Pessoa
class Pessoa:
    """Classe base para representar uma pessoa."""

    def __init__(self, nome: str, telefone: str, email: str):
        # Comando raise ValueError: "imprime" a mensagem e interrompe a continuação do código
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string não vazia.")
        if not telefone or not isinstance(telefone, str):
            raise ValueError("Telefone deve ser uma string não vazia.")
        if not email or not isinstance(email, str):
            raise ValueError("Email deve ser uma string não vazia.")

        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        """Retorna uma representação em string da pessoa."""
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
        )

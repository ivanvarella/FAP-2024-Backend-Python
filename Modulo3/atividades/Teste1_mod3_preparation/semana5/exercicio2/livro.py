class Livro:
    def __init__(self, titulo, autor, ano, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano
        self.numero_paginas = numero_paginas

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Número de Páginas: {self.numero_paginas}"

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Número de Páginas: {self.numero_paginas}")

    def abrir_livro(self, pagina):
        if pagina <= self.numero_paginas:
            print(f"Livro {self.titulo} abrerto na página {pagina}.")
        else:
            print(
                f"Página inexistente. Este livro só possui {self.numero_paginas} páginas."
            )

    def fechar_livro(self):
        print(f"Livro {self.titulo} fechado.")


def main():
    # Criação de vários objetos Livro
    livro1 = Livro("O Alquimista", "Paulo Coelho", 1988, 208)
    livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899, 256)
    livro3 = Livro("A Revolução dos Bichos", "George Orwell", 1945, 152)
    livro4 = Livro("1984", "George Orwell", 1949, 328)
    livro5 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96)

    # Lista de livros para iteração
    livros = [livro1, livro2, livro3, livro4, livro5]

    # Demonstração do uso dos métodos __str__, exibir_detalhes, abrir_livro e fechar_livro
    for livro in livros:
        print(livro)  # Exibe a representação em string do livro
        print("-" * 40)
        livro.exibir_detalhes()  # Exibe os detalhes do livro
        print("-" * 40)
        livro.abrir_livro(50)  # Tenta abrir o livro na página 50
        livro.fechar_livro()  # Fecha o livro
        print("=" * 40)  # Separador entre os livros

    # Testando a abertura de um livro em uma página inexistente
    print("\nTestando a abertura de uma página inexistente:")
    livro5.abrir_livro(
        100
    )  # Tentativa de abrir uma página além do número total de páginas


main()

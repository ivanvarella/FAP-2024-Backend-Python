import crud as banco


# # Inserir um livro
# banco.inserir_livro(
#     "O Grande Livro", "Disponível", 2023, "2023-01-01", "Nenhuma observação", 0, 1
# )

# Ler todos os livros
# livros = banco.ler_livros()
# print("Livros na tabela:", livros)

# Ler um livro específico
livro = banco.ler_livro_por_id(10)
print("Livro com ID 1:", livro)

# Atualizar um livro
# banco.atualizar_livro(
#     1,
#     "O Grande Livro Atualizado",
#     "Emprestado",
#     2023,
#     "2023-01-02",
#     "Observação atualizada",
#     1,
#     1,
# )

# Deletar um livro
# banco.deletar_livro(1)

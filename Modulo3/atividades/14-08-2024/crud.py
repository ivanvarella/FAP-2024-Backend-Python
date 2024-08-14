import sqlite3


# Função para conectar ao banco de dados
def conectar_db():
    return sqlite3.connect("biblioteca.db")


# # Função para criar a tabela de livros
# def criar_tabela_livros():
#     conn = conectar_db()
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS livros (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             titulo TEXT NOT NULL,
#             estado_do_livro TEXT NOT NULL,
#             ano INTEGER,
#             data_aquisicao DATE,
#             observacao TEXT,
#             lido INTEGER,
#             editora_id INTEGER,
#             FOREIGN KEY(editora_id) REFERENCES editoras(id)
#         );
#         """
#     )
#     conn.commit()
#     conn.close()


# Função para inserir um livro
def inserir_livro(
    titulo, estado_do_livro, ano, data_aquisicao, observacao, lido, editora_id
):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO livros (titulo, estado_do_livro, ano, data_aquisicao, observacao, lido, editora_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (titulo, estado_do_livro, ano, data_aquisicao, observacao, lido, editora_id),
    )
    conn.commit()
    conn.close()


# Função para ler todos os livros
def ler_livros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return livros


# Função para ler um livro específico por ID
def ler_livro_por_id(livro_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
    livro = cursor.fetchone()
    conn.close()
    return livro


# Função para atualizar um livro
def atualizar_livro(
    livro_id, titulo, estado_do_livro, ano, data_aquisicao, observacao, lido, editora_id
):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE livros
        SET titulo = ?, estado_do_livro = ?, ano = ?, data_aquisicao = ?, observacao = ?, lido = ?, editora_id = ?
        WHERE id = ?
        """,
        (
            titulo,
            estado_do_livro,
            ano,
            data_aquisicao,
            observacao,
            lido,
            editora_id,
            livro_id,
        ),
    )
    conn.commit()
    conn.close()


# Função para deletar um livro
def deletar_livro(livro_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()

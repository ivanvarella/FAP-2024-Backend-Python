from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

caminho_arquivo = os.path.join(os.getcwd(), "livros.db")

# print(f"Caminho do arquivo: {caminho_arquivo}")
# print(f"O diretório existe? {os.path.exists(os.path.dirname(caminho_arquivo))}")
# print(
#     f"Tenho permissão de escrita? {os.access(os.path.dirname(caminho_arquivo), os.W_OK)}"
# )

app = Flask(__name__)


# Configuração do banco de dados
def get_db_connection():
    # Cria o banco se não existir ou aponta para ele caso exista
    conn = sqlite3.connect(caminho_arquivo)
    conn.row_factory = sqlite3.Row
    return conn


# Criar a tabela se ela não existir
def init_db():
    conn = get_db_connection()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT NOT NULL)"
    )
    conn.close()


init_db()

print(f"O banco de dados foi criado? {os.path.exists(caminho_arquivo)}")


@app.route("/")
def index():
    conn = get_db_connection()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return render_template("index.html", livros=livros)


@app.route("/adicionar", methods=["GET", "POST"])
def adicionar_livro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO livros (titulo, autor) VALUES (?, ?)", (titulo, autor)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("adicionar.html")


@app.route("/excluir/<int:livro_id>")
def excluir_livro(livro_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/editar/<int:livro_id>", methods=["GET", "POST"])
def editar_livro(livro_id):
    conn = get_db_connection()
    livro = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,)).fetchone()
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        conn.execute(
            "UPDATE livros SET titulo = ?, autor = ? WHERE id = ?",
            (titulo, autor, livro_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    conn.close()
    return render_template("editar.html", livro=livro)


if __name__ == "__main__":
    app.run(debug=True)

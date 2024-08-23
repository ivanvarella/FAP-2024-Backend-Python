import sqlite3
from datetime import datetime
import os

# Obtém o caminho completo do diretório onde o arquivo atual está localizado
caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
# Caminho para o banco de dados SQLite onde as tarefas serão armazenadas
CAMINHO_BANCO = os.path.join(caminho_diretorio, "dados_banco.db")


def conectar():
    """Estabelece uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DataAbertura TEXT NOT NULL,
            Nome TEXT NOT NULL,
            TipoCont INTEGER NOT NULL,
            Saldo FLOAT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

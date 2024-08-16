import sqlite3
import os

# Caminho para o banco de dados SQLite onde as tarefas serão armazenadas
CAMINHO_BANCO = os.path.join(os.getcwd(), "Avant", "tarefas.db")


def conectar():
    """Estabelece uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    """Cria a tabela de tarefas no banco de dados SQLite, caso ela não exista."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DataIn TEXT,
            DataFim TEXT,
            Descricao TEXT NOT NULL,
            prioridade INTEGER,
            status INTEGER,
            obs TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def criar_tabela():
    """Cria a tabela de tarefas se ela não existir."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DataIn TEXT NOT NULL,
            DataFim TEXT,
            Descricao TEXT NOT NULL,
            prioridade INTEGER NOT NULL,
            status TEXT NOT NULL,
            obs TEXT
        )
    """
    )
    conn.commit()
    conn.close()


criar_tabela()

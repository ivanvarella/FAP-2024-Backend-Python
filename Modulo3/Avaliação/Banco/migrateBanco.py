import sqlite3
import os
from datetime import datetime


def criar_tabela_contas(conn):
    """Cria a tabela de contas no banco de dados."""
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_conta INTEGER UNIQUE NOT NULL,
            data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
            nome TEXT NOT NULL,
            tipo_conta INTEGER NOT NULL,
            saldo REAL NOT NULL DEFAULT 0.0,
            ativa BOOLEAN DEFAULT 1
        )
    """
    )


def criar_tabela_operacoes(conn):
    """Cria a tabela de operações no banco de dados."""
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS operacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            tipo_movimentacao TEXT NOT NULL,
            valor REAL NOT NULL,
            id_conta INTEGER NOT NULL,
            FOREIGN KEY(id_conta) REFERENCES contas(id)
        )
    """
    )


def criar_banco_de_dados():
    """Cria o banco de dados SQLite e as tabelas necessárias."""
    try:
        # Caminho para o banco de dados
        caminho_banco = os.path.join(os.path.dirname(__file__), "banco.db")

        # Conecta ao banco de dados
        conn = sqlite3.connect(caminho_banco)

        # Cria as tabelas
        criar_tabela_contas(conn)
        criar_tabela_operacoes(conn)

        # Confirma as alterações
        conn.commit()

        print("Banco de dados criado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e} (código de erro: {e.args[0]})")
    finally:
        if conn:
            conn.close()


# Chamar a função para criar o banco de dados
criar_banco_de_dados()

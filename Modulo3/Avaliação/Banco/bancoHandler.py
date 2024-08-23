import sqlite3
import os
from datetime import datetime


# Obtém o caminho completo do diretório onde o arquivo atual está localizado
caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
# Caminho para o banco de dados SQLite
CAMINHO_BANCO = os.path.join(caminho_diretorio, "Banco.db")


def conectar():
    """Estabelece uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_conta INTEGER UNIQUE NOT NULL,
            data_abertura DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
            nome TEXT NOT NULL,
            tipo_conta BOOLEAN NOT NULL,
            saldo DECIMAL(12, 2) NOT NULL,
            ativa BOOLEAN NOT NULL DEFAULT (1)
        )
        """
    )
    conn.commit()
    conn.close()


class BancoHandler:
    def __init__(self, nome, tipo_conta, saldo=0, limite_especial=0):
        self.nome = nome
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite_especial = limite_especial

    def inserir_conta(nome, saldo, tipo_conta):
        conn = conectar()
        cursor = conn.cursor()

        # Encontra o próximo número de conta disponível
        cursor.execute("SELECT COALESCE(MAX(numero_conta), 0) + 1 FROM contas")
        numero_conta = cursor.fetchone()[0]

        # Insere a nova conta na tabela
        cursor.execute(
            """
            INSERT INTO contas (numero_conta, nome, saldo, tipo_conta)
            VALUES (?, ?, ?, ?)
            """,
            (numero_conta, nome, saldo, tipo_conta),
        )

        conn.commit()
        conn.close()

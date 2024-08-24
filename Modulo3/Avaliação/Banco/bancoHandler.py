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
    """Cria as tabelas de contas e operações no banco de dados, se elas não existirem."""
    with conectar() as conn:
        cursor = conn.cursor()

        # Cria a tabela de contas
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

        # Cria a tabela de operações
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

        conn.commit()


class BancoHandler:
    def __init__(self, nome, tipo_conta, saldo=0, limite_especial=0):
        self.nome = nome
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite_especial = limite_especial

    def inserir_conta(nome, saldo, limite_especial, tipo_conta):
        conn = conectar()
        cursor = conn.cursor()

        # Encontra o próximo número de conta disponível
        cursor.execute("SELECT COALESCE(MAX(numero_conta), 0) + 1 FROM contas")
        numero_conta = cursor.fetchone()[0]

        # Insere a nova conta na tabela
        cursor.execute(
            """
            INSERT INTO contas (numero_conta, nome, saldo, limite_especial, tipo_conta)
            VALUES (?, ?, ?, ?, ?)
            """,
            (numero_conta, nome, saldo, limite_especial, tipo_conta),
        )

        conn.commit()
        conn.close()

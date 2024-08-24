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


class Conta:
    def __init__(self, nome, saldo=0, limite_especial=0, tipo_conta=1):
        """Inicializa uma conta com saldo e limite especial."""
        self.nome = nome
        self.data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.saldo = saldo
        self.limite_especial = limite_especial
        self.tipo_conta = tipo_conta  # 1: Conta Corrente / 2: Conta Poupança

    def criar_conta(self):
        """Cria uma nova conta no banco de dados."""

        self.operações = [(self.data_abertura, "ABERTURA DE CONTA", self.saldo)]

        with conectar() as conn:
            cursor = conn.cursor()

            # Encontra o próximo número de conta disponível
            cursor.execute("SELECT COALESCE(MAX(numero_conta), 0) + 1 FROM contas")
            numero_conta = cursor.fetchone()[0]
            self.numero_conta = numero_conta

            # Insere a nova conta na tabela
            cursor.execute(
                """
                INSERT INTO contas (numero_conta, nome, saldo, tipo_conta)
                VALUES (?, ?, ?, ?)
                """,
                (self.numero_conta, self.nome, self.saldo, self.tipo_conta),
            )

            conn.commit()

    # def depositar(self, valor):
    #     """Deposita um valor na conta, deve ser positivo."""
    #     if valor > 0:
    #         self.saldo += valor
    #         self.registrar_operacao("DEPÓSITO", valor)
    #     else:
    #         print("O valor do depósito deve ser positivo.")

    # def sacar(self, valor):
    #     """Saca um valor da conta, utilizando o limite especial se necessário."""
    #     if valor <= 0:
    #         print("O valor do saque deve ser positivo.")
    #         return

    #     if self.saldo >= valor:
    #         self.saldo -= valor
    #         self.registrar_operacao("SAQUE", -valor)
    #     elif self.saldo + self.limite_especial >= valor:
    #         self.saldo -= valor
    #         self.registrar_operacao("SAQUE LIMITE", -valor)
    #         print(
    #             f"Saldo insuficiente. Usando limite especial. Novo saldo: R${self.saldo:.2f}"
    #         )
    #     else:
    #         print(
    #             f"Saldo insuficiente. Seu saldo atual é de R${self.saldo:.2f} e seu limite especial é de R${self.limite_especial:.2f}."
    #         )

    # def registrar_operacao(self, tipo, valor):
    #     """Registra uma operação na tabela de operações."""
    #     with conectar() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             """
    #             INSERT INTO operacoes (tipo_movimentacao, valor, id_conta)
    #             VALUES (?, ?, (SELECT id FROM contas WHERE numero_conta = ?))
    #             """,
    #             (tipo, valor, self.numero_conta),
    #         )
    #         conn.commit()

    # def exibir_saldo(self):
    #     """Exibe o saldo atual da conta."""
    #     print(f"Saldo atual: R${self.saldo:.2f}")

    # def extrato(self):
    #     """Exibe o extrato das operações realizadas na conta."""
    #     with conectar() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             """
    #             SELECT data_movimentacao, tipo_movimentacao, valor
    #             FROM operacoes
    #             WHERE id_conta = (SELECT id FROM contas WHERE numero_conta = ?)
    #             """,
    #             (self.numero_conta,),
    #         )
    #         operacoes = cursor.fetchall()

    #     print(f"Extrato CC N° {self.numero_conta}\n")
    #     for operacao in operacoes:
    #         data, descricao, valor = operacao
    #         print(f"{data} {descricao:<20} R${valor:10.2f}")
    #     print(f"\nSaldo atual: R${self.saldo:.2f}\n")


# Testes:
criar_tabela()  # Cria as tabelas no banco de dados se não existirem

# Criando uma nova conta
objConta = Conta(nome="João Silva", saldo=1000, limite_especial=500, tipo_conta=1)

# Criando uma instância da conta e realizando operações
# conta = Conta(nome="João Silva", saldo=1000, tipo_conta=1)
# conta.depositar(500)
# conta.sacar(200)
# conta.exibir_saldo()
# conta.extrato()

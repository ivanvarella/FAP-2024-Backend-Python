# Obter o IP do Windows dentro do WSL usando PowerShell
import subprocess

# Conexão com o banco de dados MySQL
import mysql.connector
from mysql.connector import Error

# Função: calcular idade (anos, meses e dias)
from datetime import datetime, timedelta

# =======================================


# Obter o IP do Windows dentro do WSL usando PowerShell
def get_windows_ip():
    try:
        # Executa o comando PowerShell para obter o IP do Windows
        result = subprocess.run(
            [
                "powershell.exe",
                "-Command",
                'Get-NetIPAddress | Where-Object { $_.InterfaceAlias -eq "Ethernet" -and $_.AddressFamily -eq "IPv4" } | Select-Object -ExpandProperty IPAddress',
            ],
            capture_output=True,
            text=True,
        )

        # Verifica se o comando foi executado com sucesso
        if result.returncode != 0:
            raise Exception("Erro ao executar o comando PowerShell")

        # Extrai o endereço IP da saída do comando
        ip_address = result.stdout.strip()
        if not ip_address:
            raise Exception("Não foi possível obter o endereço IP")

        return ip_address

    except Exception as e:
        print(f"Erro: {e}")
        return None


# =======================================

# windows_ip = get_windows_ip()
# if windows_ip:
#     print(f"IP do Windows: {windows_ip}")
# else:
#     print("Não foi possível obter o IP do Windows")


## Função para validação de entradas input
# - msg: mensagem mostrada no input
# - tipoEsperado: "string", "int", "float", "intFloat" - "intFloat" podendo receber int ou float
# - aceitaVazio: padrão False (não aceitando valors vazios), caso aceite, declarar True - Não faz nenhuma verificação
# - Retorno da função: valor, erroTipo, erroVazio, msgErro
def isValidInput(msg, tipoEsperado, aceitaVazio=False):

    # Futuros aprimoramentos:
    # 1- Função isValid:
    #   - Receber listas e realizar validações
    #   - Receber int ou float com range limitado, por exemplo: validar se número está entre 1 e 10, muito útil para o caso de opções a fins
    #   - Como o retorno da função está ficando muito extenso, alterar o retorno para retornar uma lista com todos os retornos juntos

    # Inicialização dos erros:
    erroTipo = False
    erroVazio = False
    erroMsg = ""
    valor = input(msg)

    while True:
        # Verifica se está vazio e se deveria estar: Não aceita mas está?  Erro
        if (aceitaVazio == False) and (len(valor) == 0):
            erroMsg = "Entrada vazia não é permitida."
            print(erroMsg)
            valor = input(msg)
        # Verifica se está vazio e se deveria estar: Aceita vazio e está vazio? Tudo certo!
        # Não verifica mais nada!
        elif (aceitaVazio == True) and (len(valor) == 0):
            erroTipo = False
            erroVazio = False
            break
        else:
            # Se o tipo esperado for string, todos os valores são aceitos
            if tipoEsperado == "string":
                erroTipo = False
                break
            elif tipoEsperado == "int":
                try:
                    valor = int(valor)
                    erroTipo = False
                    break
                except ValueError:
                    erroTipo = True
                    erroMsg = "Entrada inválida. O valor deve ser um inteiro."
                    print(erroMsg)
                    valor = input(msg)
            elif tipoEsperado == "float":
                try:
                    valor = float(valor)
                    erroTipo = False
                    break
                except ValueError:
                    erroTipo = True
                    erroMsg = "Entrada inválida. O valor deve ser um float."
                    print(erroMsg)
                    valor = input(msg)
            elif tipoEsperado == "intFloat":
                try:
                    valor = float(valor)
                    erroTipo = False
                    break
                except ValueError:
                    erroTipo = True
                    erroMsg = "Entrada inválida. O valor deve ser um número."
                    print(erroMsg)
                    valor = input(msg)

    return valor, erroTipo, erroVazio, erroMsg


# =======================================

# MySQL - WorkBech:
# host_windows = get_windows_ip()

# db_config = {
#     "host": host_windows,  # Ip do Windows!
#     "port": "3307",
#     "user": "root",
#     "password": "123321",
#     "database": "ativ.04-08_age",
# }


def connect_to_database(db_config):
    """
    Estabelece a conexão com o banco de dados MySQL.

    Retorna:
        connection: Objeto de conexão do MySQL.
    """
    try:
        connection = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
            port=db_config["port"],
        )

        if connection.is_connected():
            print(
                f"Conexão estabelecida com sucesso ao banco de dados MySQL - {db_config['database']}."
            )
            return connection
    except Error as e:
        print("Erro ao conectar ao banco de dados MySQL:", e)
        return None


def create_data(connection, query, data):
    """
    Insere novos dados na tabela especificada.

    Args:
        connection: Objeto de conexão do MySQL.
        query: Consulta SQL para inserção.
        data: Dados a serem inseridos.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Dados inseridos com sucesso.")
    except Error as e:
        print("Erro ao inserir dados:", e)
    finally:
        cursor.close()


def read_data(connection, query):
    """
    Lê dados da tabela especificada.

    Args:
        connection: Objeto de conexão do MySQL.
        query: Consulta SQL para leitura.

    Retorna:
        rows: Dados lidos da tabela.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print("Erro ao ler dados:", e)
        return None
    finally:
        cursor.close()


def update_data(connection, query, data):
    """
    Atualiza dados na tabela especificada.

    Args:
        connection: Objeto de conexão do MySQL.
        query: Consulta SQL para atualização.
        data: Dados a serem atualizados.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Dados atualizados com sucesso.")
    except Error as e:
        print("Erro ao atualizar dados:", e)
    finally:
        cursor.close()


def delete_data(connection, query, data):
    """
    Deleta dados da tabela especificada.

    Args:
        connection: Objeto de conexão do MySQL.
        query: Consulta SQL para deleção.
        data: Dados a serem deletados.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Dados deletados com sucesso.")
    except Error as e:
        print("Erro ao deletar dados:", e)
    finally:
        cursor.close()


# Utilização:
# connection = connect_to_database(db_config)

# if connection:
#     # Exemplo de inserção
#     # insert_query = "INSERT INTO livros (id, titulo, estado_do_livro, ano) VALUES (%s, %s, %s, %s)"
#     # data_to_insert = (126, "Novo Livro", "Disponível", 2024)
#     # create_data(connection, insert_query, data_to_insert)

#     # Exemplo de leitura
#     select_query = "SELECT * FROM livros"
#     rows = read_data(connection, select_query)
#     if rows:
#         for row in rows:
#             print(row)

#     # Exemplo de atualização
#     # update_query = "UPDATE livros SET estado_do_livro = %s WHERE id = %s"
#     # data_to_update = ("Emprestado", 126)
#     # update_data(connection, update_query, data_to_update)

#     # Exemplo de deleção
#     # delete_query = "DELETE FROM livros WHERE id = %s"
#     # data_to_delete = (126,)
#     # delete_data(connection, delete_query, data_to_delete)

#     # Fechar a conexão
#     connection.close()
#     print("Conexão ao banco de dados encerrada.")


# =======================================


def calcular_idade_completa(nome, data_nascimento):
    """
    Calcula a idade de uma pessoa em anos, meses e dias com base na data de nascimento fornecida.

    Args:
        nome (str): O nome da pessoa.
        data_nascimento (str): A data de nascimento no formato "dd/mm/aaaa".

    Retorna:
        str: Uma mensagem com o nome e a idade da pessoa em anos, meses e dias.
    """
    try:
        # Converte a string da data de nascimento para um objeto datetime
        data_nascimento_dt = datetime.strptime(data_nascimento, "%d/%m/%Y")

        # Obtém a data atual
        data_atual = datetime.now()

        # Calcula a diferença em anos
        anos = data_atual.year - data_nascimento_dt.year
        # Ajusta se ainda não teve o aniversário no ano corrente
        if (data_atual.month, data_atual.day) < (
            data_nascimento_dt.month,
            data_nascimento_dt.day,
        ):
            anos -= 1

        # Calcula a diferença em meses e dias
        meses = data_atual.month - data_nascimento_dt.month
        if data_atual.day < data_nascimento_dt.day:
            meses -= 1

        if meses < 0:
            meses += 12

        dias = data_atual.day - data_nascimento_dt.day
        if dias < 0:
            # Obtém o último dia do mês anterior
            ultimo_dia_mes_anterior = (
                data_atual.replace(day=1) - timedelta(days=1)
            ).day
            dias += ultimo_dia_mes_anterior

        return nome, anos, meses, dias

    except ValueError as e:
        return f"Erro ao processar a data de nascimento: {e}"

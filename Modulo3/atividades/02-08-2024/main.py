import mysql.connector
from mysql.connector import Error

# Dados para configuração da conexão com o banco de dados MySQL
# Rasp:
# db_config = {
#     "host": "192.168.50.1",
#     "port": "3306",
#     "user": "root",
#     "password": "123321",
#     "database": "biblioteca",
# }

# MySQL - WorkBech:
db_config = {
    "host": "192.168.50.19",  # Ip do Windows!
    "port": "3307",
    "user": "root",
    "password": "123321",
    "database": "biblioteca",
}


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


if __name__ == "__main__":
    connection = connect_to_database(db_config)

    if connection:
        # Exemplo de inserção
        # insert_query = "INSERT INTO livros (id, titulo, estado_do_livro, ano) VALUES (%s, %s, %s, %s)"
        # data_to_insert = (126, "Novo Livro", "Disponível", 2024)
        # create_data(connection, insert_query, data_to_insert)

        # Exemplo de leitura
        select_query = "SELECT * FROM livros"
        rows = read_data(connection, select_query)
        if rows:
            for row in rows:
                print(row)

        # Exemplo de atualização
        # update_query = "UPDATE livros SET estado_do_livro = %s WHERE id = %s"
        # data_to_update = ("Emprestado", 126)
        # update_data(connection, update_query, data_to_update)

        # Exemplo de deleção
        # delete_query = "DELETE FROM livros WHERE id = %s"
        # data_to_delete = (126,)
        # delete_data(connection, delete_query, data_to_delete)

        # Fechar a conexão
        connection.close()
        print("Conexão ao banco de dados encerrada.")

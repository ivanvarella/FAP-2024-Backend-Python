import mysql.connector
from mysql.connector import Error


def connect_to_database():
    try:
        # Estabeleça a conexão com o banco de dados
        connection = mysql.connector.connect(
            # Rasp
            host="192.168.50.1",
            user="root",  # Substitua por seu nome de usuário do MySQL
            password="123321",  # Substitua pela sua senha do MySQL
            database="biblioteca",  # Substitua pelo nome do banco de dados que você deseja acessar
            # PC - MariaDB
            # host="127.0.0.1",
            # port=3307,  # Especificar a porta correta pois é diferente da padrão (3306)
            # user="root",  # Substitua por seu nome de usuário do MySQL
            # password="123321",  # Substitua pela sua senha do MySQL
            # database="teste_db_aula",  # Substitua pelo nome do banco de dados que você deseja acessar
        )

        if connection.is_connected():
            print("Conexão estabelecida com sucesso ao banco de dados MySQL.")

            # Crie um cursor para executar consultas
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Conectado ao banco de dados:", record)

            # Exemplo de uma consulta simples
            cursor.execute(
                "SELECT * FROM usuarios;"
            )  # Substitua 'sua_tabela' pelo nome da sua tabela
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            # Feche o cursor e a conexão
            cursor.close()
            connection.close()
            print("Conexão ao banco de dados encerrada.")

    except Error as e:
        print("Erro ao conectar ao banco de dados MySQL:", e)


if __name__ == "__main__":
    connect_to_database()

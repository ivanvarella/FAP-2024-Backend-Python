import funcoesSuporte as fsuporte

# Converter da data para o formato aceito pelo MySQL
from datetime import datetime

# Configuração do banco de dados:
# MySQL - WorkBech:
host_windows = fsuporte.get_windows_ip()

db_config = {
    "host": host_windows,  # Ip do Windows!
    "port": "3307",
    "user": "root",
    "password": "123321",
    "database": "ativ.04-08_age",
}


connection = None
try:
    while True:
        print("\n\nDigite 0 para encerrar o programa.\n")
        nome, _, _, _ = fsuporte.isValidInput("\nDigite o nome: ", "string")
        if nome.lower() == "0":
            break
        data_nascimento, _, _, _ = fsuporte.isValidInput(
            "\nDigite a data de nascimento (no formato: dd/mm/aaaa): ", "string"
        )
        if data_nascimento.lower() == "0":
            break

        # Recebe os dados tratados:
        nome, anos, meses, dias = fsuporte.calcular_idade_completa(
            nome, data_nascimento
        )
        print(f"{nome} tem {anos} anos, {meses} meses e {dias} dias.")

        # Convertendo a data de nascimento para o formato yyyy-mm-dd
        data_nascimento_dt = datetime.strptime(data_nascimento, "%d/%m/%Y")
        data_nascimento_formatada = data_nascimento_dt.strftime("%Y-%m-%d")

        print(f"Data de nascimento formatada: {data_nascimento_formatada}")

        # Grava no banco de dados:
        connection = fsuporte.connect_to_database(db_config)
        if connection:
            insert_query = "INSERT INTO pessoas (nome, data_nascimento) VALUES (%s, %s)"
            data_to_insert = (nome, data_nascimento_formatada)
            fsuporte.create_data(connection, insert_query, data_to_insert)
finally:
    if connection and connection.is_connected():
        connection.close()

print("\n\nPrograma encerrado.\n\n")

# windows_ip = fsuporte.get_windows_ip()
# if windows_ip:
#     print(f"IP do Windows: {windows_ip}")
# else:
#     print("Não foi possível obter o IP do Windows")

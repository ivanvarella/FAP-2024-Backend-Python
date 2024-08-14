import sqlite3


def verificar_tabelas():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    conn.close()
    print("Tabelas no banco de dados:", tabelas)


verificar_tabelas()

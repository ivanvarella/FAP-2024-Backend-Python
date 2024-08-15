import re


def validar_email(email):
    """
    Valida um endereço de e-mail usando uma expressão regular.

    :param email: Endereço de e-mail a ser validado
    :return: True se o e-mail for válido, False caso contrário
    """
    # Expressão regular para validar e-mails
    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao_email, email):
        return True
    else:
        return False


def main():
    # Exemplos de e-mails para testar
    emails_para_teste = [
        "teste@example.com",
        "exemplo@dominio.co",
        "usuario@sub.dominio.com",
        "invalido@dominio",
        "@dominio.com",
        "usuario@dominio.",
        "usuario@.dominio.com",
        "usuario@dominio.c",
    ]

    for email in emails_para_teste:
        valido = validar_email(email)
        print(f"{email} é válido? {valido}")


main()

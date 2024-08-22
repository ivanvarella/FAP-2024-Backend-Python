from datetime import datetime, timedelta


# # Obtém a data e hora atual
# agora = datetime.now()

# # Formata a data e hora em uma string legível
# data_hora_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")


def calcular_idade_completa(data_nascimento):
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

        return anos, meses, dias

    except ValueError as e:
        return f"Erro ao processar a data de nascimento: {e} - A data deve ser no formato dd/mm/aaaa."


anos, meses, dias = calcular_idade_completa("12/01/1983")

print(f"{anos} anos, {meses} meses e {dias} dias")

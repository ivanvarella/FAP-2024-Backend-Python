from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Para conseguir acessar a tabela Contas do banco de dados
# Usando o ORM do Django com a classe em models do App contas
from .models import Conta

# Importar a classe Movimentacao do models do App Movimentacoes
from movimentacoes.models import Movimentacao

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, date, timedelta

# Create your views here.


# Função formatar os valores monetários antes de salvar no DB
def formatar_valor(valor):
    """
    Converte uma string de valor monetário para um float.
    Exemplo de entrada: 'R$ 1.000.000,00'
    Exemplo de saída: 1000000.00
    """
    # Remove o símbolo 'R$' e espaços
    valor = valor.replace("R$", "").replace(" ", "")

    # Remove os pontos que são separadores de milhar
    valor = valor.replace(".", "")

    # Substitui a vírgula por ponto para a conversão
    valor = valor.replace(",", ".")

    # Converte a string para float
    try:
        valor_float = float(valor)
    except ValueError:
        raise ValueError("O valor fornecido não é um formato numérico válido")

    return valor_float


@login_required(login_url="/usuarios/logar")
def cadastrar_conta(request):

    # Via link ou direto no navegador
    if request.method == "GET":

        # Pega do models os tipos de contas para preencher no select, caso alterado já altera no form automaticamente
        TIPO_CONTA_CHOICES = Conta.TIPO_CONTA_CHOICES

        return render(
            request, "cadastrar_conta.html", {"tipo_conta_choices": TIPO_CONTA_CHOICES}
        )

    # Se for via form (retorno do cadastro para processar)
    elif request.method == "POST":

        # Dados para a tabela Conta no DB
        nome = request.POST.get("nome")
        tipo_conta = request.POST.get("tipo_conta")
        saldo = formatar_valor(request.POST.get("saldo"))
        limite_especial = formatar_valor(request.POST.get("limite_especial"))
        # Verifica se o checkbox foi marcado:retorna True ou False para salvar no DB
        ativa = request.POST.get("ativa") == "on"

        # print(
        #     f"Nome: {nome} - Tipo_conta: {tipo_conta} - Saldo: {saldo} - Limite_especial: {limite_especial} - Ativa: {ativa}"
        # )
        # return redirect("cadastrar_conta")
        # Validação dos dados
        if nome is None:
            messages.error(request, "O Campo nome é obrigatório.")
            return redirect("cadastrar_conta")

        try:
            tipo_conta = int(tipo_conta)
            saldo = float(saldo)
            limite_especial = float(limite_especial)
        except ValueError:
            messages.error(request, "Dados fornecidos são inválidos.")
            return redirect("cadastrar_conta")

        # Cria a nova conta no banco de dados
        try:
            nova_conta = Conta.objects.create(
                nome=nome,
                tipo_conta=tipo_conta,
                saldo=saldo,
                limite_especial=limite_especial,
                ativa=ativa,
            )
            messages.success(request, "Conta criada com sucesso!")
            # Fazer o redirecionar para a página de listagem de contas ou outra página
            return redirect("cadastrar_conta")  # Temporario
        except Exception as e:
            messages.error(request, f"Erro ao criar conta: {e}")
            return redirect("cadastrar_conta")

    return render(request, "cadastro_conta.html")

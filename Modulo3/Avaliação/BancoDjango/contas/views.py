from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Para conseguir acessar a tabela Contas do banco de dados
# Usando o ORM do Django com a classe em models do App contas
from .models import Conta

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, date, timedelta

# Create your views here.


@login_required(login_url="/usuarios/logar")
def cadastrar_conta(request):

    # Via link ou direto no navegador
    if request.method == "GET":
        return render(request, "cadastrar_conta.html")

    # Se for via form (retorno do cadastro para processar)
    elif request.method == "POST":
        nome = request.POST.get("nome")
        numero_conta = request.POST.get("numero_conta")
        tipo_conta = request.POST.get("tipo_conta")
        saldo = request.POST.get("saldo")
        ativa = request.POST.get("ativa") == "on"  # Verifica se o checkbox foi marcado

        # Validação dos dados
        if not nome or not numero_conta or not tipo_conta or saldo is None:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("cadastrar_conta")

        try:
            numero_conta = int(numero_conta)
            tipo_conta = int(tipo_conta)
            saldo = float(saldo)
        except ValueError:
            messages.error(request, "Dados fornecidos são inválidos.")
            return redirect("cadastrar_conta")

        # Cria a nova conta no banco de dados
        try:
            nova_conta = Conta.objects.create(
                nome=nome,
                numero_conta=numero_conta,
                tipo_conta=tipo_conta,
                saldo=saldo,
                ativa=ativa,
            )
            messages.success(request, "Conta criada com sucesso!")
            # return redirect(
            #     "listar_contas"
            # )  # Redireciona para a página de listagem de contas ou outra página
        except Exception as e:
            messages.error(request, f"Erro ao criar conta: {e}")
            return redirect("cadastrar_conta")

    return render(request, "cadastro_conta.html")

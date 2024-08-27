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

# Para conseguir tratar e enviar via contexto os dados das contas + user
# para o template de conta_cliente como Json e assim ser utilizado para
# alteração do DOM dinamicamente com Js
from django.utils.safestring import mark_safe
import json

# Para formatar_valor()
from decimal import Decimal

# Para calular saldo médio da conta
from django.db.models import Avg


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
        # valor_float = float(valor)
        valor_decimal = Decimal(valor)
    except ValueError:
        raise ValueError("O valor fornecido não é um formato numérico válido")

    return valor_decimal


# TODO Implementar os cáculos via triggers no banco
@login_required(login_url="/usuarios/logar")
def calcular_saldo_medio(movimentacoes):

    # Calcula a média dos saldos_antes e saldo_apos
    saldo_medio = movimentacoes.aggregate(
        media_saldo_antes=Avg("saldo_antes"), media_saldo_apos=Avg("saldo_apos")
    )

    # Calcula a média geral dos saldos
    saldo_medio_total = (
        saldo_medio["media_saldo_antes"] + saldo_medio["media_saldo_apos"]
    ) / 2

    return saldo_medio_total


@login_required(login_url="/usuarios/logar")
def cadastrar_conta(request):

    # Via link ou direto no navegador
    if request.method == "GET":

        # Pega do models os tipos de contas para preencher no select, caso alterado já altera no form automaticamente
        TIPO_CONTA_CHOICES = Conta.TIPO_CONTA_CHOICES
        usuarios_banco = User.objects.values(
            "id", "first_name", "last_name", "username"
        )

        return render(
            request,
            "cadastrar_conta.html",
            {
                "tipo_conta_choices": TIPO_CONTA_CHOICES,
                "usuarios_banco": usuarios_banco,
            },
        )

    # Se for via form (retorno do cadastro para processar)
    elif request.method == "POST":

        # Dados para a tabela Conta no DB
        cliente_id = request.POST.get("cliente")
        tipo_conta = request.POST.get("tipo_conta")
        saldo = formatar_valor(request.POST.get("saldo"))
        limite_especial = formatar_valor(request.POST.get("limite_especial"))
        # Verifica se o checkbox foi marcado:retorna True ou False para salvar no DB
        ativa = request.POST.get("ativa") == "on"

        try:
            tipo_conta = int(tipo_conta)
            saldo = float(saldo)
            limite_especial = float(limite_especial)
        except ValueError:
            messages.error(request, "Dados fornecidos são inválidos.")
            return redirect("cadastrar_conta")

        # Cria a nova conta no banco de dados
        try:

            # Obtém a instância do User usando o ID do cliente
            usuario = User.objects.get(id=cliente_id)

            nova_conta = Conta.objects.create(
                id_user=usuario,
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


@login_required(login_url="/usuarios/logar")
def editar_conta(request, numero_conta):
    # Regata os dados da Conta para preencher os inputs de acordo com os dados do Banco
    dados_conta_cliente = Conta.objects.get(numero_conta=numero_conta)

    # Resgata os dados do cliente da Conta
    dados_cliente = User.objects.get(id=dados_conta_cliente.id_user.id)

    # Resgata os dados CHOICES da models
    TIPO_CONTA_CHOICES = Conta.TIPO_CONTA_CHOICES

    # Flag para edição de conta
    editar_conta = True

    # Via link ou direto no navegador
    if request.method == "GET":

        return render(
            request,
            "cadastrar_conta.html",
            {
                "tipo_conta_choices": TIPO_CONTA_CHOICES,
                "dados_conta_cliente": dados_conta_cliente,
                "dados_cliente": dados_cliente,
                "editar_conta": editar_conta,
            },
        )

    elif request.method == "POST":
        conta = get_object_or_404(Conta, numero_conta=numero_conta)

        # Resgatando os dados do formulário de edição de conta
        limite_especial = formatar_valor(request.POST.get("limite_especial"))
        ativa = request.POST.get("ativa") == "on"

        try:
            # Atualizando os campos específicos
            conta.limite_especial = Decimal(limite_especial)
            conta.ativa = ativa

            conta.save()
            messages.success(request, "Conta atualizada com sucesso.")
        except ValueError:
            messages.error(
                request, "Erro ao atualizar a conta. Verifique os valores inseridos."
            )
            return render(
                request,
                "cadastrar_conta.html",
                {
                    "tipo_conta_choices": TIPO_CONTA_CHOICES,
                    "dados_conta_cliente": dados_conta_cliente,
                    "dados_cliente": dados_cliente,
                    "editar_conta": editar_conta,
                },
            )

        return redirect("listar_contas")


@login_required(login_url="/usuarios/logar")
def conta_cliente(request):

    # Verifia se o user tem contas cadastradas
    try:
        dados_conta_cliente_verificacao = Conta.objects.get(id_user=request.user.id)
    except Conta.DoesNotExist:
        messages.warning(request, "Conta não encontrada.")
        return redirect("cadastrar_conta")

    # Via link ou direto no navegador
    if request.method == "GET":
        dados_conta_cliente = Conta.objects.get(id_user=request.user.id)
        dados_cliente = User.objects.get(id=request.user.id)
        # Apesar as últimas 3 movimentações da conta
        dados_movimentacoes = Movimentacao.objects.filter(
            conta=dados_conta_cliente
        ).order_by("-data_movimentacao")[:3]
        tipo_movimentacao_choices = Movimentacao.TIPO_MOVIMENTACAO_CHOICES

        # Obter os dados para popular o select das contas para transferencia
        # select_related('id_user'): Isso faz um INNER JOIN implícito entre Conta e User,
        # garantindo que se obtenha apenas as contas que têm um usuário associado e
        # trazendo os dados desses usuários em uma única consulta ao banco de dados.
        # contas_users = Conta.objects.select_related("id_user").all()
        contas_users = (
            Conta.objects.select_related("id_user")
            .values(
                "numero_conta",
                "tipo_conta",
                "id_user__first_name",
                "id_user__last_name",
            )
            .filter(ativa=True)
        )

        tipo_conta_choices = Conta.TIPO_CONTA_CHOICES

        return render(
            request,
            "conta_cliente.html",
            {
                "dados_conta_cliente": dados_conta_cliente,
                "dados_cliente": dados_cliente,
                "dados_movimentacoes": dados_movimentacoes,
                "tipo_movimentacao_choices": tipo_movimentacao_choices,
                "contas_users": contas_users,
                "tipo_conta_choices": tipo_conta_choices,
            },
        )
    elif request.method == "POST":

        # Add a movimentacao (saque, deposito ou transferencia - Não funcionando ainda)
        operacao = request.POST.get("operacao")

        if operacao == "deposito":
            valor_deposito = formatar_valor(request.POST.get("valor_deposito"))

            # print(f"\n\n\nO valor_deposito: {valor_deposito}\n\n\n")
            # input("Pressione Enter para continuar...")

            # if valor_deposito <= 0:
            if valor_deposito <= Decimal("0.00"):
                messages.error(
                    request,
                    "Valor de depósito inválido.\nNão é possível realizar o depósito de R$ 0,00 reais.",
                )
            else:
                dados_conta_cliente = Conta.objects.get(id_user=request.user.id)
                saldo = Decimal(dados_conta_cliente.saldo)
                # saldo = float(dados_conta_cliente.saldo)

                # Calcula novo saldo após operação de depósito
                saldo_atualizado = saldo + valor_deposito
                data_atual = datetime.now()

                # Salva a movimentação no banco
                try:
                    nova_movimentacao = Movimentacao.objects.create(
                        conta=dados_conta_cliente,
                        tipo_movimentacao=2,  # Depósito
                        valor=valor_deposito,
                        data_movimentacao=data_atual,
                    )

                    # Atualiza o saldo da conta no banco
                    dados_conta_cliente.saldo = saldo_atualizado
                    dados_conta_cliente.save()

                    messages.success(request, "Depósto realizado com sucesso!")

                except Exception as e:
                    # Não precisa redirecionar aqui pois está renderizando a página no final com a mensagem de erro
                    messages.error(request, f"Erro ao tentar realizar o depósito: {e}")

        elif operacao == "saque":
            valor_saque = formatar_valor(request.POST.get("valor_saque"))
            # valor_saque = float(formatar_valor(request.POST.get("valor_saque")))
            # if valor_saque <= 0:
            if valor_saque <= Decimal("0.00"):
                messages.error(
                    request,
                    "Valor de saque inválido.\nNão é possível realizar o saque de R$ 0,00 reais.",
                )
            else:
                sacou = False
                dados_conta_cliente = Conta.objects.get(id_user=request.user.id)
                saldo = Decimal(dados_conta_cliente.saldo)
                limite_especial = Decimal(dados_conta_cliente.limite_especial)
                # saldo = float(dados_conta_cliente.saldo)
                # limite_especial = float(dados_conta_cliente.limite_especial)

                # print(f"\n\nValor de saque do input formatado: {valor_saque}\n\n")
                # novo_valor_input = request.POST.get("valor_saque")
                # print(
                #     f"\n\nValor de saque do input antes de formatar: {novo_valor_input}\n\n"
                # )

                # Possui saldo suficiente
                if saldo >= valor_saque:
                    saldo_atualizado = saldo - valor_saque
                    data_atual = datetime.now()
                    messages.success(request, "Saque realizado com sucesso!")
                    sacou = True
                # O saldo é insuficiente mas possui limite no limite_especial
                elif saldo + limite_especial >= valor_saque:
                    saldo_atualizado = (
                        saldo - valor_saque
                    )  # Fica negativo no limite do saldo+limite_especial
                    data_atual = datetime.now()
                    messages.warning(
                        request,
                        "Saque realizado com sucesso!\nUtilizando o limite especial da conta.",
                    )
                    sacou = True
                # Não possui saldo ou limite especial o suficiente
                # Não faz nada e re-renderiza a página
                else:
                    maximo_disponivel = saldo + limite_especial
                    messages.error(
                        request,
                        f"Saldo insuficiente. Seu saldo atual é de R${saldo:.2f} e seu limite especial é de R${limite_especial:.2f}.\nO máximo disponível para saque é de R${maximo_disponivel:.2f}.",
                    )

                if sacou:
                    try:
                        nova_movimentacao = Movimentacao.objects.create(
                            conta=dados_conta_cliente,
                            tipo_movimentacao=3,  # Saque
                            valor=valor_saque,
                            data_movimentacao=data_atual,
                        )

                        # Atualiza o saldo da conta no banco
                        dados_conta_cliente.saldo = saldo_atualizado
                        dados_conta_cliente.save()

                    except Exception as e:
                        # Não precisa redirecionar aqui pois está renderizando a página no final com a mensagem de erro
                        messages.error(request, f"Erro ao tentar realizar o saque: {e}")

        elif operacao == "transferencia":
            pass

        # Após salvar (success) ou não (fail), recarrega a página com a mensagem:
        # Obter os dados atualizados para envio para o template
        dados_conta_cliente = Conta.objects.get(id_user=request.user.id)
        dados_cliente = User.objects.get(id=request.user.id)
        # Apesar as últimas 3 movimentações da conta
        dados_movimentacoes = Movimentacao.objects.filter(
            conta=dados_conta_cliente
        ).order_by("-data_movimentacao")[:3]
        tipo_movimentacao_choices = Movimentacao.TIPO_MOVIMENTACAO_CHOICES
        tipo_conta_choices = Conta.TIPO_CONTA_CHOICES

        # Fetch com INNER JOIN de contas e user se as contas estiverem ativas
        contas_users = (
            Conta.objects.select_related("id_user")
            .values(
                "numero_conta",
                "tipo_conta",
                "id_user__first_name",
                "id_user__last_name",
            )
            .filter(ativa=True)
        )

        # Redirecionar para o conta_cliente com os dados de contexto atualizados
        return render(
            request,
            "conta_cliente.html",
            {
                "dados_conta_cliente": dados_conta_cliente,
                "dados_cliente": dados_cliente,
                "dados_movimentacoes": dados_movimentacoes,
                "tipo_movimentacao_choices": tipo_movimentacao_choices,
                "contas_users": contas_users,
                "tipo_conta_choices": tipo_conta_choices,
            },
        )


@login_required(login_url="/usuarios/logar")
def extrato(request, numero_conta):
    # Via link ou direto no navegador
    # Recupera a conta com base no número da conta
    dados_conta_cliente = get_object_or_404(Conta, numero_conta=numero_conta)
    # Recupera o usuário associado à conta
    dados_cliente = dados_conta_cliente.id_user
    tipo_movimentacao_choices = Movimentacao.TIPO_MOVIMENTACAO_CHOICES

    # Para vizualização dos filtros aplicados no momento
    periodo_aplicado = "Todo o período"
    tipo_aplicado = "Todos"

    # Resgata as movimentacoes para calculo do saldo médio e calcula
    movimentacoes_saldo_medio = Movimentacao.objects.filter(
        conta=dados_conta_cliente
    ).order_by("-data_movimentacao")
    saldo_medio = calcular_saldo_medio(movimentacoes_saldo_medio)

    # Via link ou direto no navegador
    if request.method == "GET":
        # Busca todas as movimentações associadas à conta
        # dados_movimentacoes = Movimentacao.objects.filter(conta=dados_conta_cliente)
        dados_movimentacoes = Movimentacao.objects.filter(
            conta=dados_conta_cliente
        ).order_by("-data_movimentacao")

        # Conta o número de movimentações
        numero_de_movimentacoes = dados_movimentacoes.count()

    elif request.method == "POST":
        # Recupera os valores do formulário
        periodo = request.POST.get("periodo")
        tipo_movimentacao = request.POST.get("tipo")

        # Filtra as movimentações com base no período selecionado
        if periodo == "5min":
            tempo_inicio = datetime.now() - timedelta(minutes=5)
            periodo_aplicado = "Últimos 5 minutos"
        elif periodo == "30min":
            tempo_inicio = datetime.now() - timedelta(minutes=30)
            periodo_aplicado = "Últimos 30 minutos"
        elif periodo == "2h":
            tempo_inicio = datetime.now() - timedelta(hours=2)
            periodo_aplicado = "Últimas 2 horas"
        elif periodo == "5h":
            tempo_inicio = datetime.now() - timedelta(hours=5)
            periodo_aplicado = "Últimas 5 horas"
        elif periodo == "24h":
            tempo_inicio = datetime.now() - timedelta(hours=24)
            periodo_aplicado = "Últimas 24 horas"
        elif periodo == "2d":
            tempo_inicio = datetime.now() - timedelta(days=2)
            periodo_aplicado = "Últimos 2 dias"
        elif periodo == "5d":
            tempo_inicio = datetime.now() - timedelta(days=5)
            periodo_aplicado = "Últimos 5 dias"
        else:
            # Todo o período
            tempo_inicio = None
            periodo_aplicado = "Todo o período"

        # Filtro base
        filtros = {"conta": dados_conta_cliente}

        # Aplica o filtro de período
        if tempo_inicio:
            # Sufixo __gte no Django ORM significa "greater than or equal to"
            filtros["data_movimentacao__gte"] = tempo_inicio

        # Aplica o filtro de tipo de movimentação, se não for "todos"
        if tipo_movimentacao and tipo_movimentacao != "todos":
            filtros["tipo_movimentacao"] = tipo_movimentacao
            tipo_aplicado = dict(tipo_movimentacao_choices).get(
                int(tipo_movimentacao), "Todos"
            )

        # print(f"\n\nFiltros aplicados: {filtros}\n\n")
        # Filtros aplicados: {'conta': <Conta: Id do usuário: admin - Número da conta: 626013 - Saldo: 1500.00>, 'tipo_movimentacao': '2'}

        # Recupera as movimentações filtradas
        dados_movimentacoes = Movimentacao.objects.filter(**filtros).order_by(
            "-data_movimentacao"
        )

        numero_de_movimentacoes = dados_movimentacoes.count()

    # Renderiza a página com GET ou POST
    return render(
        request,
        "extrato.html",
        {
            "dados_conta_cliente": dados_conta_cliente,
            "dados_movimentacoes": dados_movimentacoes,
            "dados_cliente": dados_cliente,
            "tipo_movimentacao_choices": tipo_movimentacao_choices,
            "numero_de_movimentacoes": numero_de_movimentacoes,
            "periodo_aplicado": periodo_aplicado,
            "tipo_aplicado": tipo_aplicado,
            "saldo_medio": saldo_medio,
        },
    )


@login_required(login_url="/usuarios/logar")
def listar_contas(request):
    # Via link ou direto no navegador
    if request.method == "GET":

        # Pega do models os tipos de contas e os dados para preencher no select, caso alterado já altera no form automaticamente
        dados_contas = Conta.objects.all()
        TIPO_CONTA_CHOICES = Conta.TIPO_CONTA_CHOICES

        return render(
            request,
            "listar_contas.html",
            {
                "dados_contas": dados_contas,
                "tipo_conta_choices": TIPO_CONTA_CHOICES,
            },
        )

    return render(request, "listar_contas.html")

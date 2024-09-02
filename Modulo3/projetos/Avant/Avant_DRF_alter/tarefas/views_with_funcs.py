from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Para conseguir acessar a tabela Tarefas do banco de dados
# Usando o ORM do Django com a classe em models do App Tarefas
from .models import Tarefas

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, date, timedelta

# Create your views here.


@login_required(login_url="/usuarios/logar")
def cadastrar_tarefa(request):

    # Se o usuário não estiver autenticado -> Redirect para logar
    # if not request.user.is_authenticated:
    #     return redirect("/usuarios/logar")

    # Quando acessado diretamente via link ou digitando direto
    if request.method == "GET":
        status_choices = Tarefas.status_choices
        prioridade_choices = Tarefas.prioridade_choices
        return render(
            request,
            "cadastrar_tarefa.html",
            {
                "status_choices": status_choices,
                "prioridade_choices": prioridade_choices,
            },
        )
    # Quando a página recarregar após executar o action do form para cadastrar a tarefa
    elif request.method == "POST":
        # Obtém os dados do formulário
        descricao = request.POST.get("descricao")
        status = int(request.POST.get("status"))
        prioridade = int(request.POST.get("prioridade"))
        obs = request.POST.get("obs")
        dataLimite = request.POST.get("dataLimite")  # Convertendo para datetime

        # Validação dos dados (opcional, adicione aqui)
        if not descricao:
            messages.add_message(
                request, constants.ERROR, "Preencha todos os campos obrigatórios."
            )

        # Concluído
        if status == 3:
            dataFim = datetime.now().date()
            progresso_conclusao = 100
        else:
            dataFim = None
            progresso_conclusao = int(request.POST.get("progresso_conclusao"))

        try:
            dataLimite = datetime.strptime(
                dataLimite, "%Y-%m-%d"
            ).date()  # Convertendo para data
        except ValueError:
            messages.add_message(
                request,
                constants.ERROR,
                "Data Limite inválida. Utilize o formato DD-MM-YYYY.",
            )
            return render(request, "cadastrar_tarefa.html")

        # Obtém o usuário logado
        user = request.user

        # Cria a tarefa
        # Não precisa colocar a dataInicio pois já é inserido ao criar, pela classe no models
        tarefa = Tarefas.objects.create(
            descricao=descricao,
            status=status,
            prioridade=prioridade,
            obs=obs,
            progresso_conclusao=progresso_conclusao,
            dataLimite=dataLimite,
            dataFim=dataFim,
            user=user,
        )

        messages.add_message(
            request, constants.SUCCESS, "Tarefa cadastrada com sucesso!"
        )
        return redirect("listar_tarefas")
    else:
        return render(request, "cadastrar_tarefa.html")


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)
    if tarefa.user == request.user:
        if request.method == "POST":
            # Obtém os dados do formulário POST
            descricao = request.POST.get("descricao")
            status = int(request.POST.get("status"))
            prioridade = int(request.POST.get("prioridade"))
            obs = request.POST.get("obs")
            dataLimite = request.POST.get("dataLimite")

            # Validação dos dados:
            # Concluído
            # Se mudou para 3 -> Atualiza a dataFim
            if status == 3:
                dataFim = datetime.now().date()
                progresso_conclusao = 100
            # Se era 3 ou mudou para outro valor != de 3 -> Atualiza a dataFim para None
            else:
                dataFim = None
                progresso_conclusao = int(request.POST.get("progresso_conclusao"))

            try:
                dataLimite = datetime.strptime(dataLimite, "%Y-%m-%d").date()
            except ValueError:
                messages.add_message(
                    request,
                    constants.ERROR,
                    "Data Limite inválida. Utilize o formato DD-MM-YYYY.",
                )
                return render(
                    request,
                    "editar_tarefa.html",
                    {
                        "tarefa_editar": tarefa,
                        "status_choices": Tarefas.status_choices,
                        "prioridade_choices": Tarefas.prioridade_choices,
                    },
                )

            # Atualiza os dados da tarefa que foi obtida pelo get_object_or_404
            tarefa.descricao = descricao
            tarefa.status = status
            tarefa.prioridade = prioridade
            tarefa.obs = obs
            tarefa.progresso_conclusao = progresso_conclusao
            tarefa.dataLimite = dataLimite
            tarefa.dataFim = dataFim

            tarefa.save()  # Salva as alterações no banco de dados

            messages.add_message(
                request, constants.SUCCESS, "Tarefa editada com sucesso!"
            )
            return redirect("listar_tarefas")
        else:
            status_choices = Tarefas.status_choices
            prioridade_choices = Tarefas.prioridade_choices
            return render(
                request,
                "cadastrar_tarefa.html",
                {
                    "tarefa_editar": tarefa,
                    "status_choices": status_choices,
                    "prioridade_choices": prioridade_choices,
                },
            )
    else:
        messages.add_message(
            request, constants.ERROR, "Você não tem permissão para editar esta tarefa."
        )
        return redirect("listar_tarefas")


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)

    # Verifica se a tarefa pertence ao usuário atual:
    if tarefa.user == request.user:
        # Altera o status da tarefa para 4 (Excluído)
        tarefa.status = 4
        tarefa.save()  # Salva as alterações
        messages.add_message(request, constants.SUCCESS, "Tarefa excluída com sucesso!")
    else:
        messages.add_message(
            request, constants.ERROR, "Você não tem permissão para excluir esta tarefa."
        )
    return redirect("listar_tarefas")


def listar_tarefas(request):
    # Se o usuário não estiver autenticado -> Redirect para logar
    if not request.user.is_authenticated:
        return redirect("/usuarios/logar")

    tarefas = (
        Tarefas.objects.filter(user=request.user)
        .exclude(status=4)
        .order_by("dataInicio")
    )  # Filtra as tarefas do usuário logado
    hoje = date.today()
    data_alerta = hoje + timedelta(days=3)  # Calcula a data com 3 dias a mais
    return render(
        request,
        "listar_tarefas.html",
        {"tarefas": tarefas, "hoje": hoje, "data_alerta": data_alerta},
    )

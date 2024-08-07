from django.shortcuts import render, redirect

# Importar os selects do models
from .models import Empresas

# Importar as constantes de mensagens do Django
from django.contrib import messages

# Importar os tipos de mensagens do Django
from django.contrib.messages import constants


# Create your views here.
def cadastrar_empresa(request):

    if not request.user.is_authenticated:
        return redirect("/usuarios/logar")

    if request.method == "GET":
        # print(Empresas.tempo_existencia_choices)
        return render(
            request,
            "cadastrar_empresa.html",
            {
                "tempo_existencia": Empresas.tempo_existencia_choices,
                "areas": Empresas.area_choices,
            },
        )
    elif request.method == "POST":

        # ToDo: Realizar validação de campos

        nome = request.POST.get("nome")
        cnpj = request.POST.get("cnpj")
        site = request.POST.get("site")
        tempo_existencia = request.POST.get("tempo_existencia")
        descricao = request.POST.get("descricao")
        data_final = request.POST.get("data_final")
        percentual_equity = request.POST.get("percentual_equity")
        estagio = request.POST.get("estagio")
        area = request.POST.get("area")
        publico_alvo = request.POST.get("publico_alvo")
        valor = request.POST.get("valor")
        pitch = request.FILES.get("pitch")
        logo = request.FILES.get("logo")

        try:
            empresa = Empresas(
                user=request.user,
                nome=nome,
                cnpj=cnpj,
                site=site,
                tempo_existencia=tempo_existencia,
                descricao=descricao,
                data_final_captacao=data_final,
                percentual_equity=percentual_equity,
                estagio=estagio,
                area=area,
                publico_alvo=publico_alvo,
                valor=valor,
                pitch=pitch,
                logo=logo,
            )
            empresa.save()
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            return redirect("/empresarios/cadastrar_empresa")

        messages.add_message(request, constants.SUCCESS, "Empresa criada com sucesso")
        return redirect("/empresarios/cadastrar_empresa")


def listar_empresas(request):

    if not request.user.is_authenticated:
        return redirect("/usuarios/logar")

    if request.method == "GET":

        # ToDo: Realizar os filtros das empresas

        empresas = Empresas.objects.filter(user=request.user)
        return render(request, "listar_empresas.html", {"empresas": empresas})

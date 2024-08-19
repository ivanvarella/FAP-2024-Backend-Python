from django.shortcuts import render, redirect

from django.http import HttpResponse

# Importar a classe referente a tabela usuarios que já vem no Django
from django.contrib.auth.models import User

# Importar as constantes de mensagens do Django
from django.contrib import messages

# Importar os tipos de mensagens do Django
from django.contrib.messages import constants

# Importar o Auth
from django.contrib import auth

# Para verificação do email:
import re


def is_valid_email(email):
    # Padrão de regex para validação de email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Verifica se o email corresponde ao padrão
    if re.match(pattern, email):
        return True
    else:
        return False


# Create your views here.


def cadastro(request):
    # print(f"Tipo de requisição: {request.method}")  # Imprime o tipo de requisição: GET, POST
    if request.method == "GET":  # Verifica se a requisição é do tipo GET
        return render(request, "cadastro.html")  # Renderiza um template HTML
    elif request.method == "POST":
        # debug:
        # username = request.POST.get("username")
        # senha = request.POST.get("senha")
        # confirmar_senha = request.POST.get("confirmar_senha")
        # email = request.POST.get("email")
        # nome = request.POST.get("nome")
        # sobrenome = request.POST.get("sobrenome")

        # return HttpResponse(
        #     """
        #     Todos os requests:
        #     username: {}
        #     senha: {}
        #     confirmar_senha: {}
        #     email: {}
        #     nome: {}
        #     sobrenome: {}
        #     """.format(
        #         username, senha, confirmar_senha, email, nome, sobrenome
        #     )
        # )

        # Verifica se a requisição é do tipo POST - do form cadastro.html
        username = request.POST.get(
            "username"
        )  # Obtém o valor do campo username do formulário
        senha = request.POST.get("senha")  # Obtém o valor do campo senha do formulário
        confirmar_senha = request.POST.get(
            "confirmar_senha"
        )  # Obtém o valor do campo confirmar_senha do formulário

        # Se a senha for !=  da confirmação
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não coincidem")
            return redirect("/usuarios/cadastro")

        # Se a senha tiver menos de 6 caracteres
        if len(senha) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha precisa ter pelo menos 6 digitos"
            )
            return redirect("/usuarios/cadastro")

        # Verificação de e-mail válido
        email = request.POST.get("email")
        if not is_valid_email(email):
            messages.add_message(request, constants.ERROR, "E-mail inválido")
            return redirect("/usuarios/cadastro")

        # Nome e sobrenome pode ser de qualquer jeito
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")

        # Carrega todos o users do DB com aquele username
        users = User.objects.filter(username=username)

        # print(users.exists())

        # Se já existir, dá erro e redireciona para a página de cadastro
        if users.exists():
            messages.add_message(
                request, constants.ERROR, "Já existe um usuário com esse username"
            )
            return redirect("/usuarios/cadastro")

        # Caso esteja tudo certo: cria o usuário, salva no DB e redireciona para a página de login
        user = User.objects.create_user(
            username=username, password=senha, first_name=nome, last_name=sobrenome
        )
        return redirect("/usuarios/logar")


def logar(request):

    if request.method == "GET":
        return render(request, "logar.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        # return HttpResponse(
        #     """
        #     Todos os requests:
        #     username: {}
        #     senha: {}
        #     user: {}
        #     """.format(
        #         username, senha, user
        #     )
        # )

        if user:
            auth.login(
                request, user
            )  # Verifica o usuário atrelado ao ip e o login (Sessão?)
            # Depois de criar o App tarefas, redireciona para a página de tarefas do usuario
            # return redirect("/tarefas/listar_tarefas")
            # Por enquanto, só mostrar qualquer coisa se o login der certo!
            return HttpResponse("Logou corretamente!!!!")

        messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos")
        return redirect("/usuarios/logar")

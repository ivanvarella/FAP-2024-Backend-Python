from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

# Importar a classe referente a tabela usuarios que já vem no Django
from django.contrib.auth.models import User

# Importar as constantes de mensagens do Django
from django.contrib import messages

# Importar os tipos de mensagens do Django
from django.contrib.messages import constants

# Importar o Auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Para deslogar
from django.contrib.auth import logout

# Para editar o usuario:
from django.contrib.auth import update_session_auth_hash

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


# @login_required(login_url="/usuarios/logar")
def cadastro(request):
    # print(f"Tipo de requisição: {request.method}")  # Imprime o tipo de requisição: GET, POST
    if request.method == "GET":  # Verifica se a requisição é do tipo GET
        return render(request, "cadastro.html")  # Renderiza um template HTML
    elif request.method == "POST":

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

        messages.add_message(request, constants.SUCCESS, "Usuário criado com sucesso!")

        # Login automático
        login(request, user)

        return redirect("listar_contas")


@login_required(login_url="/usuarios/logar")
def editar_usuario(request):
    if request.method == "GET":
        # Obtém os dados do usuário logado
        user = request.user

        # Renderiza o template de cadastro com os dados do usuário preenchidos
        dados_usuario = {
            "username": user.username,
            "nome": user.first_name,
            "sobrenome": user.last_name,
            "email": user.email,
        }
        return render(
            request, "cadastro.html", {"dados_usuario": dados_usuario}
        )  # Use o mesmo template de cadastro

    elif request.method == "POST":
        # Atualiza os dados do usuário no banco de dados
        user = request.user
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("nome")
        user.last_name = request.POST.get("sobrenome")
        user.email = request.POST.get("email")

        senha = request.POST.get("senha")  # Obtém o valor do campo senha do formulário
        confirmar_senha = request.POST.get("confirmar_senha")

        # Se a senha não for vazia, faça as validações
        if senha:
            # Se erro: redireciona para a mesma página com os dados que foram inseridos e msg de erro
            if senha != confirmar_senha:
                messages.add_message(
                    request, constants.ERROR, "As senhas não coincidem"
                )
                # Retorna à página de edição com mensagens de erro
                dados_usuario = {
                    "username": user.username,
                    "nome": user.first_name,
                    "sobrenome": user.last_name,
                    "email": user.email,
                }
                return render(
                    request, "cadastro.html", {"dados_usuario": dados_usuario}
                )

            # Se erro: redireciona para a mesma página com os dados que foram inseridos e msg de erro
            elif len(senha) < 6:
                messages.add_message(
                    request, constants.ERROR, "A senha precisa ter pelo menos 6 dígitos"
                )
                # Retorna à página de edição com mensagens de erro
                dados_usuario = {
                    "username": user.username,
                    "nome": user.first_name,
                    "sobrenome": user.last_name,
                    "email": user.email,
                }
                return render(
                    request, "cadastro.html", {"dados_usuario": dados_usuario}
                )

            else:
                # Atualiza a senha do usuário
                user.set_password(senha)
                update_session_auth_hash(
                    request, user
                )  # Atualiza a sessão de autenticação com a nova senha
                messages.add_message(
                    request, constants.SUCCESS, "Senha atualizada com sucesso!"
                )

        # Salva as outras alterações no banco
        user.save()

        # Caso tudo certo, redireciona para cadastrar_conta com a msg de sucesso
        messages.add_message(
            request, constants.SUCCESS, "Usuário atualizado com sucesso!"
        )
        return redirect("cadastrar_conta")


def logar(request):

    if request.user.is_authenticated:
        messages.add_message(
            request,
            constants.SUCCESS,
            f"{request.user.first_name}, você já está logado. Caso queira alternar a conta, faça logout primeiro.",
        )
        return redirect("conta_cliente")

    if request.method == "GET":
        return render(request, "logar.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(
                request, user
            )  # Verifica o usuário atrelado ao ip e o login (Sessão?)
            return redirect("/contas/conta_cliente")
            # return HttpResponse("Logou corretamente!!!!")

        messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos")
        return redirect("/usuarios/logar")


@login_required(login_url="/usuarios/logar")
def deslogar(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, "Logout realizado com sucesso!")
    return redirect("logar")  # Redirecione para a página home após o logout

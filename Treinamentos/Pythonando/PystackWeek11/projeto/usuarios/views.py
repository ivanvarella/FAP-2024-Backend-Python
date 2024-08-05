from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def cadastro(request):
    # print(request.META)  # Imprime na página os dados da requisição
    # return HttpResponse("Olá Mundo!")  # Imprime na página
    return render(request, "cadastro.html")  # Renderiza um template HTML

from django.shortcuts import render


# Create your views here.
def home(request):
    print(request.method)  # Mostra a request do usuário no terminal
    return render(request, "home.html")

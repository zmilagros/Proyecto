from django.shortcuts import render

# Create your views here.
from .models import Cliente


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto =  {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)
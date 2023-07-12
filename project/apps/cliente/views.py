from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Cliente, Pais

from .forms import ClienteForm


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto =  {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)

def crear_clientes(request):
    from datetime import date

    p1 = Pais(nombre="Argentina")
    p2 = Pais(nombre="México")
    p3 = Pais(nombre="Chile")
    
    p1.save()
    p2.save()
    p3.save()

    c1 = Cliente(nombre="Maria", apellido="Arraras", nacimiento=date(1977,9,14), pais_origen_id=p1)
    c2 = Cliente(nombre="Milagros", apellido="Arraras", nacimiento=date(2001,5,14), pais_origen_id=p2)
    c3 = Cliente(nombre="Felipe", apellido="Polzella", nacimiento=date(1998,12,25), pais_origen_id=p3)
    c4 = Cliente(nombre="Jose", apellido="Hector", nacimiento=date(1940,10,29), pais_origen_id=p1)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home")

def crear_cliente(request: HttpRequest) -> HttpResponse:
    
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

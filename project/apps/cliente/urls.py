from django.urls import path

from .views import busqueda, crear_clientes, crear_cliente, home

app_name = "cliente"       

urlpatterns = [
    path("", home, name="home" ),
    path('crear_clientes/', crear_clientes, name="crear_clientes"),
    path('crear/', crear_cliente, name="crear"),
    path('busqueda/', busqueda, name="busqueda"),
]

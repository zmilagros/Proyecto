from django.urls import path

from .views import home, crear_clientes, home, crear_cliente

app_name = "cliente"       

urlpatterns = [
    path("", home, name="home" ),
    path('crear_clientes/', crear_clientes, name="crear_clientes"),
    path('crear/',crear_cliente, name="crear"),
]

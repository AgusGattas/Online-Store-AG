from django.shortcuts import render
from .carro import Carro
from TiendaApp.models import Producto
from django.shortcuts import redirect


# Create your views here.

def agregar_producto(request, producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("TIENDA")

def eliminar_producto(request, producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("TIENDA")

def restar_producto(request, producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.restar(producto=producto)

    return redirect("TIENDA")

def limpiar_producto(request, producto_id):
    carro= Carro(request)
    
    carro.limpiar()

    return redirect("TIENDA")
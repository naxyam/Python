from django.shortcuts import render

from .carro import carro

from tienda.models import Producto

from django.shortcuts import redirect


def agregar_producto(request, producto_id)
	carro = carro(request)

	producto= Producto.objects.get(id=producto_id)

	carro.agregar(producto=producto)

	return redirect('tienda')


def eliminar_producto(request, producto_id)
	carro = carro(request)

	producto= Producto.objects.get(id=producto_id)

	carro.eliminar(producto=producto)

	return redirect('tienda')

def restar_producto(request, producto_id)
	carro = carro(request)

	producto= Producto.objects.get(id=producto_id)

	carro.restar_producto(producto=producto)

	return redirect('tienda')


def limpiar_carro(request, producto_id)
	carro = carro(request)

	carro=limpiar_carro(request)

	return redirect('tienda')
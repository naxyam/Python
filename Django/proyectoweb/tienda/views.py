from django.shortcuts import render, HttpResponse
from .models import Producto



def tienda(request):

	productos=Producto.objects.all()

	return render(request,'tienda/tienda.html')
# Create your views here.

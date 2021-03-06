from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

def busqueda_productos(request):
	return render(request,'busqueda_productos.html')

def buscar(request):

	if request.GET['prd']:

		#mensaje='Artículo buscado: %r' %request.GET["prd"]
		producto=request.GET['prd']

		if len(producto)>20:
			mensaje='Texto de búsqueda demasiado largo'

		else:

			articulos=Articulo.objects.filter(nombre__icontains=producto)
			return render(request, 'resultados_busqueda.html',{'articulos':articulos, 'query':producto})
	else:


		mensaje='No has introducido nada'

	return HttpResponse(mensaje)


def contacto(request):

	if request.method=='POST':

		miFormulario=FormularioContacto(request.POST)

		if miFormulario.is_valid():
			infForm=miFormulario.cleaned_data
			return render(request, 'gracias.html')
	else:

		miFormulario=FormularioContacto()

	return render(request, 'formulario_contacto.html', {'form':miFormulario})	

	'''Este codigo es para el formulario manual contacto.html
		subject=request.POST['asunto']
		message=request.POST['mensaje']+' '+ request.POST['email']

		email_from=settings.EMAIL_HOST_USER
		recipient_list=['naxyam@hotmail.com']

		send_mail(subject, message, email_from, recipient_list)


		return render(request, 'gracias.html')

		
	return render(request, 'contacto.html')'''
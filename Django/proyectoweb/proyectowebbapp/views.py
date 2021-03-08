from django.shortcuts import render, HttpResponse


def home(request):


	return render(request,'proyectowebbapp/home.html')



	

def tienda(request):


	return render(request,'proyectowebbapp/tienda.html')


def blog(request):


	return render(request,'proyectowebbapp/blog.html')


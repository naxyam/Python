from django.shortcuts import render
from blog.models import Categoria
from blog.models import Post, Categoria

# Create your views here.


def blog(request):
	posts=Post.objects.all()
	return render(request,'blog/blog.html',{'posts': posts})


def categoria(request, categoria_id):
	categoria=Categoria.objects.get(id=categoria_id)
	posts=Post.objects.filter(Categorias=categoria)
	return render(request,'blog/categoria.html',{'categoria':categoria,'posts': posts})
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'cursoC.html', {'dameFecha': fecha_actual})
def cursoCSS(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'cursoCSS.html', {'dameFecha': fecha_actual})


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):# primera vista
    p1 = Persona('Profesor Manuel ', 'Diaz')
    #nombre = 'Juan'
    #apellido = 'Diaz'
    temasdelCurso=[]
    ahora = datetime.datetime.now()
    #doc_externo=open('C:/Users/Natalia/Documents/Django/miProject/miProject/plantillas/miplantilla.html')
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = get_template('miPlantilla.html')

    #ctx = Context({'nombre_persona': p1.nombre, 'apellido_persona':p1.apellido, 'momento_actual': ahora, 'temas': temasdelCurso})

    #documento= doc_externo.render({'nombre_persona': p1.nombre, 'apellido_persona':p1.apellido, 'momento_actual': ahora, 'temas': temasdelCurso})

    return render(request, 'miPlantilla.html', {'nombre_persona': p1.nombre, 'apellido_persona':p1.apellido, 'momento_actual': ahora, 'temas': temasdelCurso})

def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento= '''<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>'''% fecha_actual

    return HttpResponse(documento)
    

def calculaEdad(request, agno):

    edadActual = 18
    periodo = agno-2019
    edadFutura = edadActual + periodo
    documento = '''<html><body><h2>En el año %s tendrás %s años</h2></body></html>'''%(agno, edadFutura)

    return HttpResponse(documento)

from django.shortcuts import render, redirect
from pre_entrega3.models import Alumno, Profesor , Institucion
from django.http import HttpResponse
from django.template import loader
from pre_entrega3.forms import Alumno_formulario
from pre_entrega3.forms import Profesores_formulario
from pre_entrega3.forms import Institucion_formulario
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')








def formulario_alumno(request):
    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos['nombre'], comision=datos["comision"])
            alumno.save()
            return redirect('confirmacion')
    
    return render(request,"alumnos.html")





def confirmacion(request):
    return render(request ,'confirmacion.html')







def formulario_profesor(request):
    if request.method == "POST":
        mi_formulario = Profesores_formulario(request)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], legajo=datos["legajo"])
            profesor.save()
            
            return redirect('confirmacion')
    
    return render(request, "profesores.html")





def formulario_institucion(request):
    
    if request.method == "POST":
        mi_formulario = Institucion_formulario(request)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            instituto = Institucion(ciudad=datos["ciudad"], telefono=datos["telefono"])
            instituto.save()
            
            return redirect('confirmacion.html')
    
    return render(request, "instituciones.html")




def ver_opciones(request):
    return render(request, 'datos.html')




def mostrar_datos_alumnos(request):
    alumnos= Alumno.objects.all()
    dicc = {"alumnos":alumnos}
    plantilla = loader.get_template("read_alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def mostrar_datos_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesor":profesores}
    plantilla = loader.get_template("read_profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def mostrar_datos_instituciones(request):
    instituciones = Institucion.objects.all()
    dicc = {"instituciones":instituciones}
    plantilla = loader.get_template("read_instituciones.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda_alumnos.html" , {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    
def busqueda_opciones(request):
    return render(request, 'opciones_busqueda.html')

def buscar_profesores(request):
    
    return render(request, 'busqueda_profesores.html')

def buscar_instituciones(request):
    
    return render(request, 'busqueda_instituciones.html')

def buscar_alumnos(request):
    
    return render(request, 'busqueda_alumnos.html')

def resultado_busqueda_alumnos(request):
    return render(request, 'resultado_busqueda_alumnos.html')
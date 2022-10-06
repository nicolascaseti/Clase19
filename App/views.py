from django.shortcuts import render


from App.models import Estudiante

# Create your views here.
def mostrar_inicio(request):
    estudiante = Estudiante(nombre="Ezequiel", apellido="Ruben", email="a") #Crear un estudiante
    estudiante.save() #Guarda en la base de datos
    contexto = {"estudiante_1": estudiante} #Lo va a usar en un contexto
    return render(request, "App/inicio.html", contexto) #Lo va a pasar en un template
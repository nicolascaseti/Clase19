from django.shortcuts import render


from App.models import Estudiante

# Create your views here.
def inicio(request):
    return render(request, "App/inicio.html")

def cursos(request):
    return render(request, "App/cursos.html")

def profesores(request):
    return render(request, "App/profesores.html")

def estudiantes(request):
    return render(request, "App/estudiantes.html")

def entregables(request):
    return render(request, "App/entregables.html")
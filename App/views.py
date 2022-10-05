from django.shortcuts import render


from App.models import Estudiante

# Create your views here.
def mostrar_inicio(request):
    return render(request, "App/inicio.html")
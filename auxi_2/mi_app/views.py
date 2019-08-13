from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'mi_app/index.html')

def pestaña(request):
	return render(request, 'mi_app/pestaña.html')

def equipo_docente(request):
	return render(request, 'mi_app/equipo_docente.html')
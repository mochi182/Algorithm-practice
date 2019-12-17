from django.shortcuts import render
from .forms import *
from algoritmo.utils import *

def vista_algoritmo(request):
	lista = ''
	form = ListaForm()
	return render(request, 'algoritmo/algoritmo.html', {'lista': lista, 'form': form})

def nueva_lista(request):
	if request.method=='POST':
		form = ListaForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			lista = cd.get('lista')
			return render(request, 'algoritmo/algoritmo.html', {'lista': lista, 'form': form})
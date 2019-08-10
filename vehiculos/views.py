from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Vehiculo

class VehiculoListView(ListView):
	model = Vehiculo

class VehiculoDetailView(DetailView):
	model = Vehiculo
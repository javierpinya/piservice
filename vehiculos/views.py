from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Vehiculo

class VehiculoListView(ListView):
	model = Vehiculo
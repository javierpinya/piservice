from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Vehiculo
from .forms import VehiculoForm
from django.urls import reverse, reverse_lazy

class VehiculoListView(ListView):
	model = Vehiculo

class VehiculoDetailView(DetailView):
	model = Vehiculo

@method_decorator(staff_member_required,name="dispatch")
class VehiculoSearchView(TemplateView):
	template_name = "vehiculos/vehiculo_form.html"
	Vehiculo_class = VehiculoForm
	success_url = reverse_lazy('vehiculos:vehiculos')
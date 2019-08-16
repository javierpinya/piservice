from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Vehiculo
from .forms import VehiculoForm
from django.urls import reverse, reverse_lazy
from .filters import VehiculoFilter

class StaffRequiredMixin(object):

	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super(VehiculoCreate, self).dispatch(request, *args, **kwargs)

class VehiculoListView(ListView):
	model = Vehiculo
	template_name = "vehiculos/vehiculo_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = VehiculoFilter(self.request.GET, queryset=self.get_queryset())
		return context

class VehiculoDetailView(DetailView):
	model = Vehiculo


@method_decorator(staff_member_required,name="dispatch")
class VehiculoBuscar(FormView):
	template_name="vehiculos/vehiculo_form.html"
	form_class = VehiculoForm
	success_url = reverse_lazy({'vehiculos:list'})

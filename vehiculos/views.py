from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Vehiculo, Cliente
from .forms import ClienteForm, VehiculoForm, VehiculoUpdateForm
from django.urls import reverse, reverse_lazy
from .filters import VehiculoFilter, ClienteFilter

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
	template_name = "vehiculos/vehiculo_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


@method_decorator(staff_member_required,name="dispatch")
class VehiculoIndex(ListView):
	model = Vehiculo
	template_name = "vehiculos/vehiculo_index.html"


@method_decorator(staff_member_required, name="dispatch")
class VehiculoUpdateView(UpdateView):
	model = Vehiculo
	template_name = "vehiculos/vehiculo_edit.html"
	form_class = VehiculoUpdateForm
	success_url = reverse_lazy('vehiculos:list')

@method_decorator(staff_member_required, name="dispatch")
class VehiculoCreateView(CreateView):
	model = Vehiculo
	template_name="vehiculos/vehiculo_form.html"
	form_class = VehiculoForm
	second_form_class = ClienteForm
	success_url = reverse_lazy('vehiculos:index')

	def get_context_data(self, **kwargs):
		context = super(VehiculoCreateView, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.POST)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.POST)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.cliente = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

@method_decorator(staff_member_required, name="dispatch")
class ClienteIndex(ListView):
	model = Vehiculo
	template_name = "vehiculos/cliente_index.html"

@method_decorator(staff_member_required, name="dispatch")
class ClienteCreateView(CreateView):
	model = Vehiculo
	template_name = "vehiculos/cliente_form.html"
	form_class = ClienteForm
	success_url = reverse_lazy('vehiculos:cliente_index')


	def get_context_data(self, **kwargs):
	    context = super(ClienteCreateView, self).get_context_data(**kwargs)
	    if 'form' not in context:
	    	context['form'] = self.form_class(self.request.POST)
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			solicitud = form.save()
			"""ojo, si hay que añadir un segundo form, copiar el método de vehiculocreateview"""
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class ClienteListView(ListView):
	model = Cliente
	template_name = "vehiculos/cliente_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = ClienteFilter(self.request.GET, queryset=self.get_queryset())
		return context

@method_decorator(staff_member_required, name="dispatch")
class ClienteVehiculoListView(ListView):
	model = Vehiculo
	template_name="vehiculos/cliente_vehiculo_list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = ClienteVehiculoFilter(self.request.GET, queryset=self.get_queryset())
		return context
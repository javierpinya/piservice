from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from vehiculos.models import Cliente, Vehiculo
from django.urls import reverse, reverse_lazy

# Create your views here.

class ProfileListView(ListView):
	model = Cliente
	second_model_form = Vehiculo
	template_name = "profiles/profile_list.html"
	success_url = reverse_lazy('profiles:list')
	#paginated_by = 6

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = VehiculoFilter(self.request.GET, queryset=self.get_queryset())
		return context


class ProfileDetailView(DetailView):
	"""
	Hay que recordar que el argumento 'dni' del kwargs, debe coincidir con el argumento de la url, en este caso /perfil/<dni>/
	"""
	model = Cliente
	template_name = "profiles/profile_detail.html"
	second_model_form = Vehiculo

	def get_object(self):
		#objeto = Cliente.objects.filter(dni=self.kwargs['dni'])

		objeto = Vehiculo.objects.filter(matricula=self.kwargs['matricula'])
		return get_object_or_404(objeto)
        
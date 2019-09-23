from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from vehiculos.models import Cliente, Vehiculo

# Create your views here.

class ProfileListView(ListView):
	model = Cliente
	template_name = "profiles/profile_list.html"
	#paginated_by = 6

class ProfileDetailView(DetailView):
	"""
	Hay que recordar que el argumento 'dni' del kwargs, debe coincidir con el argumento de la url, en este caso /perfil/<dni>/
	"""
	model = Cliente
	template_name = "profiles/profile_detail.html"

	def get_object(self):
		objeto = Cliente.objects.filter(dni=self.kwargs['dni'])
		return get_object_or_404(objeto)
        
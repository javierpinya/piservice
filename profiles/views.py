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
	Como vamos a usar un Foreign key que tiene Vehiculo pero no Cliente, usamos el modelo Vehiculo y filtramos
	por el campo foreign key cliente y, a su vez, por el atributo dni del objeto cliente mediante cliente__dni.
	Hay que recordar que el argumento 'dni' del kwargs, debe coincidir con el argumento de la url, en este caso /perfil/<dni>/
	"""
	model = Vehiculo
	template_name = "profiles/profile_detail.html"

	def get_object(self):
		objeto = Vehiculo.objects.filter(cliente__dni=self.kwargs['dni'])
		return get_object_or_404(objeto)
        
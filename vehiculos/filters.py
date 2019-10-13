import django_filters
from .models import Vehiculo, Cliente

#mirar como se puede hacer un filtro que busque en varios campos a la vez para poder buscar cualquier cosa desde un mismo objeto

class VehiculoFilter(django_filters.FilterSet):
	"""matricula = django_filters.CharFilter(lookup_expr='icontains')"""

	class Meta:
		model = Vehiculo
		"""fields = ('matricula',)"""
		fields = {	'matricula':['icontains'],
					'cliente__dni':['icontains'],
				}

class ClienteFilter(django_filters.FilterSet):
	class Meta:
		model = Cliente
		fields = {	'nombre':['icontains'],
					'apellidos': ['icontains'],
					'dni': ['icontains'],
					'movil': ['icontains'],
				}

class ClienteVehiculoFilter(django_filters.FilterSet):

	class Meta:
		model = Vehiculo
		fields = {	'cliente__dni':['icontains'],
					'cliente__apellidos':['icontains'],
					'matricula':['icontains'],
				}
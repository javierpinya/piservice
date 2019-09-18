import django_filters
from .models import Vehiculo, Cliente

#mirar como se puede hacer un filtro que busque en varios campos a la vez para poder buscar cualquier cosa desde un mismo objeto

class VehiculoFilter(django_filters.FilterSet):
	"""matricula = django_filters.CharFilter(lookup_expr='icontains')"""

	class Meta:
		model = Vehiculo
		"""fields = ('matricula',)"""
		fields = {'matricula':['icontains'],
				}

class ClienteFilter(django_filters.FilterSet):

	class Meta:
		model = Vehiculo
		fields = {'matricula':['icontains'],
					'cliente__apellidos':['icontains']
				}

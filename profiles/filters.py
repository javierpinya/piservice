import django_filters
from vehiculos.models import Vehiculo, Cliente

class ClienteVehiculoFilter(django_filters.FilterSet):

	class Meta:
		model = Cliente
		fields = {'dni':['icontains']
				}
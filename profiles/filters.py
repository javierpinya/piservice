import django_filters
from vehiculos.models import Vehiculo, Cliente

class ClienteVehiculoFilter(django_filters.FilterSet):

	class Meta:
		model = Vehiculo
		fields = {'cliente__dni':['icontains'],
					'cliente__apellidos':['icontains']
				}

class VehiculoFilter(django_filters.FilterSet):
	class Meta:
		model = Vehiculo
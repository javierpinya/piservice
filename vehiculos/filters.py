import django_filters
from .models import Vehiculo

class VehiculoFilter(django_filters.FilterSet):

	class Meta:
		model = Vehiculo
		fields = ('matricula',)
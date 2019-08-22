import django_filters
from .models import Vehiculo

#mirar como se puede hacer un filtro que busque en varios campos a la vez para poder buscar cualquier cosa desde un mismo objeto

class VehiculoFilter(django_filters.FilterSet):

	class Meta:
		model = Vehiculo
		fields = ('matricula',)
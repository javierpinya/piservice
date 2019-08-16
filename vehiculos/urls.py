from django.urls import path
from .views import VehiculoListView, VehiculoDetailView, VehiculoBuscar

vehiculos_patterns = ([
		path('lista/', VehiculoListView.as_view(), name='list'),
		path('vehiculo/<matricula>', VehiculoDetailView.as_view(), name='vehiculo'),
		path('', VehiculoBuscar.as_view(), name="buscar"),
	], 'vehiculos')
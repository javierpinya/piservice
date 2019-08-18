from django.urls import path
from .views import VehiculoListView, VehiculoDetailView, VehiculoBuscar, VehiculoUpdateView

vehiculos_patterns = ([
		path('lista/', VehiculoListView.as_view(), name='list'),
		path('vehiculo/<matricula>', VehiculoDetailView.as_view(), name='vehiculo'),
		path('editar/<int:pk>/', VehiculoUpdateView.as_view(), name='editar'),
		path('', VehiculoBuscar.as_view(), name="buscar"),
	], 'vehiculos')
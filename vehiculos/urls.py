from django.urls import path
from .views import VehiculoListView, VehiculoDetailView, VehiculoIndex, VehiculoUpdateView, VehiculoCreateView

vehiculos_patterns = ([
		path('lista/', VehiculoListView.as_view(), name='list'),
		path('vehiculo/<matricula>', VehiculoDetailView.as_view(), name='vehiculo'),
		path('editar/<int:pk>/', VehiculoUpdateView.as_view(), name='editar'),
		path('index/', VehiculoIndex.as_view(), name='index'),
		path('create/', VehiculoCreateView.as_view(), name="crear"),
	], 'vehiculos')
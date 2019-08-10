from django.urls import path
from .views import VehiculoListView, VehiculoDetailView

vehiculos_patterns = ([
		path('', VehiculoListView.as_view(), name='vehiculos'),
		path('<int:pk>/<slug:slug>/', VehiculoDetailView.as_view(), name='vehiculo'),
	], 'vehiculos')
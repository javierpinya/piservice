from django.urls import path
from .views import VehiculoListView

vehiculos_patterns = ([
		path('', VehiculoListView.as_view(), name='vehiculos'),
	], 'vehiculos')
from django.urls import path
from .views import VehiculoListView, VehiculoDetailView, VehiculoIndex, VehiculoUpdateView, VehiculoCreateView, ClienteIndex, ClienteCreateView, ClienteListView, ClienteVehiculoListView, VehiculoOrdenReparacionView, ProveedorIndex, ProveedorCreateView, ArticuloIndex, ArticuloCreateView

vehiculos_patterns = ([
		path('lista/', VehiculoListView.as_view(), name='list'),
		path('vehiculo/<int:pk>', VehiculoDetailView.as_view(), name='detalle'),
		path('editar/<matricula>/', VehiculoUpdateView.as_view(), name='editar'),
		path('orden/<matricula>/', VehiculoOrdenReparacionView.as_view(), name='ordenreparacion'),
		path('editar/<int:pk>/', VehiculoUpdateView.as_view(), name='historial'),
		path('index/', VehiculoIndex.as_view(), name='index'),
		path('create/', VehiculoCreateView.as_view(), name="crear"),
		path('cliente_index/', ClienteIndex.as_view(), name="cliente_index"),
		path('nuevo_cliente/', ClienteCreateView.as_view(), name="nuevo_cliente"),
		path('lista_clientes/', ClienteListView.as_view(), name="buscar_cliente"),
		path('lista_clientes_vehiculos/', ClienteVehiculoListView.as_view(), name="buscar_cliente_vehiculo"),
		path('proveedor_index/', ProveedorIndex.as_view(), name="proveedor_index"),
		path('proveedor_create/', ProveedorCreateView.as_view(), name="crear_proveedor"),
		path('articulo_index/', ArticuloIndex.as_view(), name="articulo_index"),
		path('articulo_create/', ArticuloCreateView.as_view(), name="crear_articulo"),
	], 'vehiculos')
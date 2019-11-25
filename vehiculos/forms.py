from django import forms
from .models import Cliente, Vehiculo, Reparacion, Articulo, Proveedor


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'apellidos',
			'dni',
			'razon_social',
			'grupo',
			'movil',
			'email',
			'web',
			'observaciones',
		]
		labels = {
			'nombre':'Nombre',
			'apellidos' : 'Apellidos',
			'dni': 'DNI',
			'razon_social': 'Razon_social',
			'grupo': 'Grupo',
			'movil': 'Móvil',
			'email': 'Email',
			'web': 'Web',
			'observaciones': 'Observaciones del cliente',
		}


class VehiculoForm(forms.ModelForm):
	
	class Meta:
		model = Vehiculo
		fields = [
			'cliente',
			'matricula',
			'marca',
			'modelo',
			'color',
			'kilometros',
			'bastidor',
			'asegurado',
			'aseguradora',
			'num_poliza',
			'tipo_motor',
			'placa_oval',
			'observaciones',
		]
		labels = {
			'cliente': 'Cliente',
			'matricula':'Matrícula',
			'marca':'Marca',
			'modelo':'Modelo',
			'color':'Color',
			'kilometros':'Kilómetros',
			'bastidor':'Bastidor',
			'asegurado':'Asegurado',
			'aseguradora':'Aseguradora',
			'num_poliza':'Número de Póliza',
			'tipo_motor':'Tipo de Motor',
			'placa_oval':'Placa Oval',
			'observaciones':'Observaciones',
		}

class VehiculoDetailForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = [
			'avatar',
			'cliente',
			'matricula',
			'marca',
			'modelo',
			'color',
			'kilometros',
			'bastidor',
			'asegurado',
			'aseguradora',
			'num_poliza',
			'tipo_motor',
			'placa_oval',
			'observaciones',
		]
		labels = {
			'avatar': 'Avatar',
			'cliente': 'Cliente',
			'matricula':'Matrícula',
			'marca':'Marca',
			'modelo':'Modelo',
			'color':'Color',
			'kilometros':'Kilómetros',
			'bastidor':'Bastidor',
			'asegurado':'Asegurado',
			'aseguradora':'Aseguradora',
			'num_poliza':'Número de Póliza',
			'tipo_motor':'Tipo de Motor',
			'placa_oval':'Placa Oval',
			'observaciones':'Observaciones',
		}
		exclude = {'created'}
		widgets = {
			'observaciones':forms.Textarea(),
		}


class VehiculoUpdateForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		exclude = ['created']

class OrdenReparacionForm(forms.ModelForm):
	class Meta:
		model = Reparacion
		exclude = ['created', 'updated']
		widgets = {
			'vehiculo':forms.TextInput(),
			'observaciones':forms.Textarea(),
		}

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		exclude = ['created', 'updated']
		widgets = {
			'observaciones':forms.Textarea(),
		}

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		exclude = ['created','updated']
		widgets = {
			'observaciones':forms.Textarea(),
		}

class SearchForm(forms.Form):
	query = forms.CharField()
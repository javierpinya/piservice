from django import forms
from .models import Cliente, Vehiculo


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'apellidos',
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


class VehiculoUpdateForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		exclude = ['created']
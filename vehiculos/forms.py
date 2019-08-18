from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
	
	class Meta:
		model = Vehiculo
		fields = ['matricula']

"""
		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control','placeholder':'Matrícula'}),
			'marca': forms.TextInput(attrs={'class':'form-control','placeholder':'Marca'}),
			'modelo': forms.TextInput(attrs={'class':'form-control','placeholder':'Modelo'}),
		}

		labels = {
			'matricula':'', 'marca':'', 'modelo':''
		}
		"""

class VehiculoUpdateForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		exclude = ['created']
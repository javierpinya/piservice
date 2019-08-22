from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser válido')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	# Vamos a validar el email para que no haya dos usuarios con el mismo correo
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Este email ya está registrado. Prueba con otro")
		return email

	"""
	Nota: Al estar extendiendo del formulario UserCreationForm, hay que tener en cuenta que
	estamos utilizando todas sus validaciones. Si, por ejemplo, añadiéramos nuestros propios widgets
	en el forms.py, estaríamos machacando su proceso de validación. Por eso hay que modificar esos
	widgets en tiempo de ejecución, es decir, en el archivo views.py
	"""

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar', 'bio', 'link']
		widgets = {
			'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'bio': forms.Textarea(attrs={'placeholder':'Biografía'}),
			'link': forms.URLInput(attrs={'placeholder':'web'}),
		}

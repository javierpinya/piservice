from django.db import models

# Create your models here.
class Vehiculo(models.Model):
	cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=7)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=20)
	color = models.CharField(max_length=15)
	ficha_tecnica = models.ForeignKey(FichaTecnica, on_delete=models.CASCADE)
	kilometros = models.PositiveIntegerField(null=False)
	bastidor = models.CharField(max_length=25)
	asegurado = models.BooleanField()
	aseguradora =models.CharField(max_length=50)
	num_poliza = models.CharField(max_length=20)
	tipo_motor = models.CharField(max_length=50)
	placa_oval = models.CharField(max_length=15)
	observaciones = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = [-'updated']
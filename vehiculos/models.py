from django.db import models
from ckeditor.fields import RichTextField

def custom_upload_to(instance, filename):
	old_instance = Vehiculo.objects.get(pk=instance.pk)
	old_intance.avatar.delete()
	return'profiles/' + filename

	
class Proveedor(models.Model):

	nombre = models.CharField(max_length=30)
	cif = models.CharField(max_length=10, null=True,blank=True)
	direccion = models.CharField(max_length=40, null=True,blank=True)
	persona_contacto = models.CharField(max_length=20, null=True,blank=True)
	movil = models.CharField(max_length=12, null=True,blank=True)
	email = models.CharField(max_length=30, null=True,blank=True)
	web = models.URLField(max_length=60, null=True,blank=True)
	cod_postal = models.CharField(max_length=5, null=True,blank=True)
	localidad = models.CharField(max_length=30, null=True,blank=True)
	provincia = models.CharField(max_length=20, null=True,blank=True)
	pais = models.CharField(max_length=20, null=True,blank=True)
	banco = models.CharField(max_length=22, null=True,blank=True)
	dir_banco = models.CharField(max_length=60, null=True,blank=True)
	ccc = models.CharField(max_length=20, null=True,blank=True)
	forma_pago = models.CharField(max_length=1, null=True,blank=True)
	medio_pago = models.CharField(max_length=20, null=True,blank=True)
	cuenta_contable = models.CharField(max_length=22, null=True,blank=True)
	cuenta_ingresos = models.CharField(max_length=22, null=True,blank=True)
	cuenta_retencion = models.CharField(max_length=22, null=True,blank=True)
	cuenta_caja = models.CharField(max_length=22, null=True,blank=True)
	irpf = models.IntegerField(null=True,blank=True)
	saldo = models.IntegerField(null=True,blank=True)
	iva = models.IntegerField(null=True,blank=True)
	intracomunitario = models.BooleanField(null=True,blank=True)
	observaciones = RichTextField(null=True,blank=True)
	alarmas = models.CharField(max_length=5, null=True,blank=True)
	nueva_alarma = models.CharField(max_length=5, null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de alta", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True)


	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return self.nombre





class Cliente(models.Model):

	avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	razon_social = models.CharField(max_length=60, null=True,blank=True)
	grupo = models.CharField(max_length=10, null=True,blank=True)
	dni = models.CharField(max_length=9, default="0")
	direccion = models.CharField(max_length=50, null=True,blank=True)
	cod_postal = models.CharField(max_length=5, null=True,blank=True)
	localidad = models.CharField(max_length=30, null=True,blank=True)
	provincia = models.CharField(max_length=20, null=True,blank=True)
	pais = models.CharField(max_length=20, null=True,blank=True)
	movil = models.CharField(max_length=12, null=True,blank=True)
	email = models.CharField(max_length=60, null=True,blank=True)
	web = models.URLField(max_length=60, null=True,blank=True)
	observaciones = RichTextField(verbose_name='Observaciones', null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de alta", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


	class Meta:
		ordering = ['-updated']

	def __str__(self):
		return self.dni + " - " + self.nombre + " " + self.apellidos


# Create your models here.
class Vehiculo(models.Model):
	# Sería interesante poder añadir tantas fotos como sean necesarias sobre un coche:
	# como avatar, libro de mantenimiento, ficha técnica, siniestros varios, etc
	# para ello, estaría bien crear un modelo de fotos con dos campos, uno foreign key para el coche
	# y otro con la imagen en sí.
	avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
	cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=7)
	marca = models.CharField(max_length=20, null=True, blank=True)
	modelo = models.CharField(max_length=20, null=True, blank=True)
	color = models.CharField(max_length=15, null=True, blank=True)
	kilometros = models.PositiveIntegerField(null=True, blank=True)
	bastidor = models.CharField(max_length=25, null=True, blank=True)
	asegurado = models.BooleanField(null=True, blank=True)
	aseguradora =models.CharField(max_length=50, null=True, blank=True)
	libro_mto = models.BooleanField(null=True, blank=True)
	num_poliza = models.CharField(max_length=20, null=True, blank=True)
	tipo_motor = models.CharField(max_length=50, null=True, blank=True)
	placa_oval = models.CharField(max_length=15, null=True, blank=True)
	observaciones = RichTextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return self.matricula

class Fotos(models.Model):
	vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

	#def __str__(self):
	#	return self.foto


class Reparacion(models.Model):

	cod_reparacion = models.IntegerField(null=True)
	vendedor_oper = models.CharField(max_length=8, null=True, blank=True)
	observaciones = RichTextField(null=True, blank=True)
	tipo_descuento = models.CharField(max_length=3, null=True, blank=True)
	fecha_cobro = models.DateTimeField(null=True, blank=True)
	fecha_reparacion = models.DateTimeField(null=True, blank=True)
	fecha_inspeccion = models.DateTimeField(null=True, blank=True)
	num_peritacion = models.CharField(max_length=12, null=True, blank=True)
	num_presupuesto = models.CharField(max_length=12, null=True, blank=True)
	num_albaran = models.CharField(max_length=12, null=True, blank=True)
	num_factura = models.CharField(max_length=12, null=True, blank=True)
	vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.cod_reparacion)

class contabilidad_cliente(models.Model):

	cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
	tarifa = models.CharField(max_length=3, default="O", null=True,blank=True)
	tipo_iva = models.SmallIntegerField(default=21, null=True,blank=True)
	descuento = models.SmallIntegerField(default=0, null=True,blank=True)
	descuento_pp = models.SmallIntegerField(default=0, null=True,blank=True)
	rec_eq = models.CharField(max_length=3, null=True,blank=True)
	cuenta_contable = models.CharField(max_length=22, null=True,blank=True)
	cuenta_ingresos = models.CharField(max_length=22, null=True,blank=True)
	cuenta_retencion = models.CharField(max_length=22, null=True,blank=True)
	cuenta_caja = models.CharField(max_length=22, null=True,blank=True)
	dias_de_pago = models.SmallIntegerField(default=0, null=True,blank=True)
	banco = models.CharField(max_length=22, null=True,blank=True)
	dir_banco = models.CharField(max_length=60, null=True,blank=True)
	ccc = models.CharField(max_length=20, null=True,blank=True)
	forma_pago = models.CharField(max_length=1, null=True,blank=True)
	medio_pago = models.CharField(max_length=20, null=True,blank=True)
	credito = models.SmallIntegerField(default=0, null=True,blank=True)
	limite_riesgo = models.SmallIntegerField(default=0, null=True,blank=True)
	liquidacion = models.SmallIntegerField(default=0, null=True,blank=True)
	comisionista = models.CharField(max_length=20, null=True,blank=True)
	comision = models.CharField(max_length=10, null=True,blank=True)

class Ficha_Tecnica(models.Model):

	vehiculo = models.ForeignKey(Vehiculo, null=True, on_delete=models.CASCADE)
	a1 = models.CharField(max_length=50, null=True, blank=True)
	a2 = models.CharField(max_length=100, null=True, blank=True)
	b1 = models.CharField(max_length=50, null=True, blank=True)
	b2 = models.CharField(max_length=100, null=True, blank=True)
	ci = models.CharField(max_length=11, null=True, blank=True)
	cl = models.CharField(max_length=4, null=True, blank=True)
	cv = models.IntegerField(null=True, blank=True)
	d1 = models.CharField(max_length=30, null=True, blank=True)
	d2 = models.CharField(max_length=60, null=True, blank=True)
	d3 = models.CharField(max_length=50, null=True, blank=True)
	d6 = models.CharField(max_length=4, null=True, blank=True)
	e = models.CharField(max_length=17, null=True, blank=True)
	ep = models.CharField(max_length=15, null=True, blank=True)
	ep1 = models.CharField(max_length=15, null=True, blank=True)
	ep2 = models.CharField(max_length=15, null=True, blank=True)
	ep3 = models.CharField(max_length=15, null=True, blank=True)
	ep4 = models.CharField(max_length=15, null=True, blank=True)
	f1 = models.CharField(max_length=6, null=True, blank=True)
	f11 = models.CharField(max_length=6, null=True, blank=True)
	f15 = models.CharField(max_length=6, null=True, blank=True)
	f2 = models.CharField(max_length=6, null=True, blank=True)
	f21 = models.CharField(max_length=6, null=True, blank=True)
	f3 = models.CharField(max_length=8, null=True, blank=True)
	f31 = models.CharField(max_length=8, null=True, blank=True)
	f4 = models.CharField(max_length=8, null=True, blank=True)
	f5 = models.CharField(max_length=8, null=True, blank=True)
	f51 = models.CharField(max_length=8, null=True, blank=True)
	f6 = models.CharField(max_length=8, null=True, blank=True)
	f61 = models.CharField(max_length=8, null=True, blank=True)
	f7 = models.CharField(max_length=8, null=True, blank=True)
	f71 = models.CharField(max_length=6, null=True, blank=True)
	f8 = models.CharField(max_length=6, null=True, blank=True)
	f81 = models.CharField(max_length=6, null=True, blank=True)
	g = models.CharField(max_length=6, null=True, blank=True)
	g1 = models.CharField(max_length=6, null=True, blank=True)
	g2 = models.CharField(max_length=6, null=True, blank=True)
	j = models.CharField(max_length=4, null=True, blank=True)
	j1 = models.CharField(max_length=30, null=True, blank=True)
	j2 = models.CharField(max_length=3, null=True, blank=True)
	j3 = models.CharField(max_length=3, null=True, blank=True)
	k = models.CharField(max_length=25, null=True, blank=True)
	k1 = models.CharField(max_length=25, null=True, blank=True)
	k2 = models.CharField(max_length=15, null=True, blank=True)
	l = models.CharField(max_length=2, null=True, blank=True)
	l0 = models.CharField(max_length=2, null=True, blank=True)
	l1 = models.CharField(max_length=2, null=True, blank=True)
	l2 = models.CharField(max_length=15, null=True, blank=True)
	m1 = models.CharField(max_length=8, null=True, blank=True)
	m4 = models.CharField(max_length=8, null=True, blank=True)
	o1 = models.CharField(max_length=6, null=True, blank=True)
	o11 = models.CharField(max_length=6, null=True, blank=True)
	o12 = models.CharField(max_length=6, null=True, blank=True)
	o13 = models.CharField(max_length=6, null=True, blank=True)
	o14 = models.CharField(max_length=6, null=True, blank=True)
	o21 = models.CharField(max_length=6, null=True, blank=True)
	o22 = models.CharField(max_length=6, null=True, blank=True)
	o23 = models.CharField(max_length=6, null=True, blank=True)
	o3 = models.CharField(max_length=11, null=True, blank=True)
	p1 = models.CharField(max_length=6, null=True, blank=True)
	p11 = models.CharField(max_length=15, null=True, blank=True)
	p2 = models.CharField(max_length=8, null=True, blank=True)
	p21 = models.CharField(max_length=8, null=True, blank=True)
	p3 = models.CharField(max_length=3, null=True, blank=True)
	p5 = models.CharField(max_length=20, null=True, blank=True)
	p51 = models.CharField(max_length=20, null=True, blank=True)
	q = models.CharField(max_length=3, null=True, blank=True)
	r = models.CharField(max_length=15, null=True, blank=True)
	s1 = models.CharField(max_length=3, null=True, blank=True)
	s11 = models.CharField(max_length=2, null=True, blank=True)
	s2 = models.CharField(max_length=3, null=True, blank=True)
	t = models.CharField(max_length=3, null=True, blank=True)
	u1 = models.CharField(max_length=5, null=True, blank=True)
	u2 = models.CharField(max_length=7, null=True, blank=True)
	v7 = models.CharField(max_length=6, null=True, blank=True)
	v8 = models.CharField(max_length=5, null=True, blank=True)
	v9 = models.CharField(max_length=8, null=True, blank=True)
	z = models.CharField(max_length=10, null=True, blank=True)
	cod417 = models.TextField(null=True, blank=True)
	num_serie = models.CharField(max_length=10, null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)
	opciones_hom_tipo = models.TextField(null=True, blank=True)
	reformas = models.TextField(null=True, blank=True)
	libre = models.IntegerField(null=True, blank=True)








class Articulo(models.Model):

	articulo = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=80, null=True, blank=True)
	stock = models.IntegerField(null=True, blank=True)
	stockable = models.BooleanField(null=True, blank=True)
	fecha_compra = models.DateTimeField(null=True, blank=True)
	reservados = models.IntegerField(null=True, blank=True)
	stock_optimo = models.IntegerField(null=True, blank=True)
	pedido_proveedor = models.IntegerField(null=True, blank=True)
	observaciones = RichTextField(null=True, blank=True)
	referencia = models.CharField(max_length=20, null=True, blank=True)
	tipo = models.CharField(max_length=1, null=True, blank=True)
	marca = models.CharField(max_length=30, null=True, blank=True)
	familia = models.CharField(max_length=1, null=True, blank=True)
	subfamilia = models.CharField(max_length=1, null=True, blank=True)
	precio_compra = models.IntegerField(null=True, blank=True)
	descuento_compra = models.IntegerField(null=True, blank=True)
	precio_coste = models.IntegerField(null=True, blank=True)
	iva = models.IntegerField(null=True, blank=True)
	precio_medio = models.IntegerField(null=True, blank=True)
	precio_venta = models.IntegerField(null=True, blank=True)
	beneficio = models.IntegerField(null=True, blank=True)
	pvp_iva = models.IntegerField(null=True, blank=True)
	proveedores = models.ForeignKey(Proveedor, null=True, on_delete=models.CASCADE)

	class Meta:
		ordering = ['articulo']

	def __str__(self):
		return self.articulo



# para la lista de reparaciones hacerlo con .html
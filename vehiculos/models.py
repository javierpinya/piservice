from django.db import models
from ckeditor.fields import RichTextField

def custom_upload_to(instance, filename):
	old_instance = Profile.objects.get(pk=instance.pk)
	old_intance.avatar.delete()
	return'profiles/' + filename


class Cliente(models.Model):
	avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	razon_social = models.CharField(max_length=60, null=True,blank=True)
	grupo = models.CharField(max_length=10, null=True,blank=True)
	dni = models.CharField(max_length=9, null=True,blank=True)
	direccion = models.CharField(max_length=50, null=True,blank=True)
	cod_postal = models.CharField(max_length=5, null=True,blank=True)
	localidad = models.CharField(max_length=30, null=True,blank=True)
	provincia = models.CharField(max_length=20, null=True,blank=True)
	pais = models.CharField(max_length=20, null=True,blank=True)
	movil = models.CharField(max_length=12, null=True,blank=True)
	email = models.CharField(max_length=60, null=True,blank=True)
	web = models.URLField(max_length=60, null=True,blank=True)
	observaciones = RichTextField(verbose_name='observaciones', null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de alta", null=True)
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


	class Meta:
		ordering = ['-updated']

	def __str__(self):
		return self.apellidos


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
	
class Proveedor(models.Model):

	nombre = models.CharField(max_length=30)
	cif = models.CharField(max_length=10)
	direccion = models.CharField(max_length=40)
	persona_contacto = models.CharField(max_length=20)
	movil = models.CharField(max_length=12)
	email = models.CharField(max_length=30)
	web = models.URLField(max_length=60)
	cod_postal = models.CharField(max_length=5)
	localidad = models.CharField(max_length=30)
	provincia = models.CharField(max_length=20)
	pais = models.CharField(max_length=20)
	banco = models.CharField(max_length=22)
	dir_banco = models.CharField(max_length=60)
	ccc = models.CharField(max_length=20)
	forma_pago = models.CharField(max_length=1)
	medio_pago = models.CharField(max_length=20)
	cuenta_contable = models.CharField(max_length=22)
	cuenta_ingresos = models.CharField(max_length=22)
	cuenta_retencion = models.CharField(max_length=22)
	cuenta_caja = models.CharField(max_length=22)
	irpf = models.IntegerField()
	saldo = models.IntegerField()
	iva = models.IntegerField()
	intracomunitario = models.BooleanField()
	observaciones = RichTextField()
	alarmas = models.CharField(max_length=5)
	nueva_alarma = models.CharField(max_length=5)

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return self.nombre
	

# Create your models here.
class Vehiculo(models.Model):

	cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=7)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=20)
	color = models.CharField(max_length=15)
	kilometros = models.PositiveIntegerField(null=True)
	bastidor = models.CharField(max_length=25)
	asegurado = models.BooleanField(null=True)
	aseguradora =models.CharField(max_length=50)
	num_poliza = models.CharField(max_length=20)
	tipo_motor = models.CharField(max_length=50)
	placa_oval = models.CharField(max_length=15)
	observaciones = RichTextField()
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.matricula



class Ficha_Tecnica(models.Model):

	vehiculo = models.ForeignKey(Vehiculo, null=True, on_delete=models.CASCADE)
	a1 = models.CharField(max_length=50)
	a2 = models.CharField(max_length=100)
	b1 = models.CharField(max_length=50)
	b2 = models.CharField(max_length=100)
	ci = models.CharField(max_length=11)
	cl = models.CharField(max_length=4)
	cv = models.IntegerField()
	d1 = models.CharField(max_length=30)
	d2 = models.CharField(max_length=60)
	d3 = models.CharField(max_length=50)
	d6 = models.CharField(max_length=4)
	e = models.CharField(max_length=17)
	ep = models.CharField(max_length=15)
	ep1 = models.CharField(max_length=15)
	ep2 = models.CharField(max_length=15)
	ep3 = models.CharField(max_length=15)
	ep4 = models.CharField(max_length=15)
	f1 = models.CharField(max_length=6)
	f11 = models.CharField(max_length=6)
	f15 = models.CharField(max_length=6)
	f2 = models.CharField(max_length=6)
	f21 = models.CharField(max_length=6)
	f3 = models.CharField(max_length=8)
	f31 = models.CharField(max_length=8)
	f4 = models.CharField(max_length=8)
	f5 = models.CharField(max_length=8)
	f51 = models.CharField(max_length=8)
	f6 = models.CharField(max_length=8)
	f61 = models.CharField(max_length=8)
	f7 = models.CharField(max_length=8)
	f71 = models.CharField(max_length=6)
	f8 = models.CharField(max_length=6)
	f81 = models.CharField(max_length=6)
	g = models.CharField(max_length=6)
	g1 = models.CharField(max_length=6)
	g2 = models.CharField(max_length=6)
	j = models.CharField(max_length=4)
	j1 = models.CharField(max_length=30)
	j2 = models.CharField(max_length=3)
	j3 = models.CharField(max_length=3)
	k = models.CharField(max_length=25)
	k1 = models.CharField(max_length=25)
	k2 = models.CharField(max_length=15)
	l = models.CharField(max_length=2)
	l0 = models.CharField(max_length=2)
	l1 = models.CharField(max_length=2)
	l2 = models.CharField(max_length=15)
	m1 = models.CharField(max_length=8)
	m4 = models.CharField(max_length=8)
	o1 = models.CharField(max_length=6)
	o11 = models.CharField(max_length=6)
	o12 = models.CharField(max_length=6)
	o13 = models.CharField(max_length=6)
	o14 = models.CharField(max_length=6)
	o21 = models.CharField(max_length=6)
	o22 = models.CharField(max_length=6)
	o23 = models.CharField(max_length=6)
	o3 = models.CharField(max_length=11)
	p1 = models.CharField(max_length=6)
	p11 = models.CharField(max_length=15)
	p2 = models.CharField(max_length=8)
	p21 = models.CharField(max_length=8)
	p3 = models.CharField(max_length=3)
	p5 = models.CharField(max_length=20)
	p51 = models.CharField(max_length=20)
	q = models.CharField(max_length=3)
	r = models.CharField(max_length=15)
	s1 = models.CharField(max_length=3)
	s11 = models.CharField(max_length=2)
	s2 = models.CharField(max_length=3)
	t = models.CharField(max_length=3)
	u1 = models.CharField(max_length=5)
	u2 = models.CharField(max_length=7)
	v7 = models.CharField(max_length=6)
	v8 = models.CharField(max_length=5)
	v9 = models.CharField(max_length=8)
	z = models.CharField(max_length=10)
	cod417 = models.TextField()
	num_serie = models.CharField(max_length=10)
	observaciones = models.TextField()
	opciones_hom_tipo = models.TextField()
	reformas = models.TextField()
	libre = models.IntegerField()








class Articulo(models.Model):

	articulo = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=80)
	stock = models.IntegerField()
	stockable = models.BooleanField()
	fecha_compra = models.DateTimeField()
	reservados = models.IntegerField()
	stock_optimo = models.IntegerField()
	pedido_proveedor = models.IntegerField()
	observaciones = RichTextField()
	referencia = models.CharField(max_length=20)
	tipo = models.CharField(max_length=1)
	marca = models.CharField(max_length=30)
	familia = models.CharField(max_length=1)
	subfamilia = models.CharField(max_length=1)
	precio_compra = models.IntegerField()
	descuento_compra = models.IntegerField()
	precio_coste = models.IntegerField()
	iva = models.IntegerField()
	precio_medio = models.IntegerField()
	precio_venta = models.IntegerField()
	beneficio = models.IntegerField()
	pvp_iva = models.IntegerField()
	proveedores = models.ManyToManyField(Proveedor)
	vehiculos = models.ManyToManyField(Vehiculo)


	class Meta:
		ordering = ['articulo']

	def __str__(self):
		return self.articulo


class Reparacion(models.Model):
	
	vehiculo = models.ForeignKey(Vehiculo, null=True, on_delete=models.CASCADE)
	cod_reparacion = models.IntegerField(null=True)
	vendedor_oper = models.CharField(max_length=8)
	observaciones = RichTextField()
	tipo_descuento = models.CharField(max_length=3)
	kilometros = models.IntegerField()
	combustible = models.CharField(max_length=4)
	asegurado = models.BooleanField()
	libro_mantenimiento = models.BooleanField()
	fecha_cobro = models.DateTimeField()
	fecha_reparacion = models.DateTimeField()
	fecha_inspeccion = models.DateTimeField()
	num_peritacion = models.CharField(max_length=12)
	num_presupuesto = models.CharField(max_length=12)
	num_albaran = models.CharField(max_length=12)
	num_factura = models.CharField(max_length=12)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True, null=True)


# para la lista de reparaciones hacerlo con .html
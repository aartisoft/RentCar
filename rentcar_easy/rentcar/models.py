from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Marcas(models.Model):
 
    nombre      = models.CharField(max_length=30)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User)


    def __str__(self):
        return self.nombre 


class TiposVehiculos(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User)
    
    def __str__(self):
        return self.nombre


class TiposCombustibles(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200, blank=True,null=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User)
    

    def __str__(self):
        return self.nombre



class Modelos(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200, blank=True,null=True)
    marca       = models.ForeignKey('Marcas',on_delete=models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User)
    

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):


    YEAR_CHOICES = (
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
    )

    descripcion = models.CharField(max_length=50)
    no_chasis   = models.CharField(max_length=25, blank=True, null=True)
    no_motor    = models.CharField(max_length=16, blank=True, null=True)
    no_placa    = models.CharField(max_length=7, blank=True, null=True)
    modelo      = models.ForeignKey('Modelos', on_delete=models.CASCADE)
    tipo        = models.ForeignKey('TiposVehiculos', on_delete=models.CASCADE)
    combustible = models.ForeignKey('TiposCombustibles',on_delete=models.CASCADE)
    anio        = models.CharField(max_length=4,choices=YEAR_CHOICES, blank=True, null=True)
    color       = models.CharField(max_length=15, blank=True, null=True)
    tarifa      = models.PositiveIntegerField(default=0)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(User)
    

    def __str__(self):
        return self.descripcion



class Clientes(models.Model):


    TYPE_PERSON_CHOISES = ( ('Fisica', 'Fisica'), ('Juridica', 'Juridica'),
    )

    SEX_CHOISES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )


    nombre          = models.CharField(max_length=30)
    cedula          = models.CharField(max_length=12)
    no_tjcredito    = models.CharField(max_length=26, blank=True, null=True)
    limite_credito  = models.PositiveIntegerField( default=0)
    tipo_persona    = models.CharField(max_length=10,choices=TYPE_PERSON_CHOISES, blank=True, null=True)
    sexo            = models.CharField(max_length=10,choices=SEX_CHOISES, blank=True, null=True)
    fecha_nacimiento= models.DateField(auto_now=False,auto_now_add=False)
    licencia        = models.CharField(max_length=16)
    direccion       = models.CharField(max_length=100, blank=True, null=True)
    create_at       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True)
    user            = models.ForeignKey(User)
    
    def __str__(self):
        return self.nombre


class Empleados(models.Model):

    nombre           = models.CharField(max_length=30)
    cedula           = models.CharField(max_length=12)
    telefono         = models.CharField(max_length=12)
    comision         = models.PositiveIntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False,auto_now_add=False)
    fecha_ingreso    = models.DateField(auto_now=False,auto_now_add=False)
    create_at        = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
    user             = models.ForeignKey(User)

    def __str__(self):
        return self.nombre


class Rerservaciones(models.Model):

    empleado             = models.ForeignKey('Empleados', on_delete=models.CASCADE)
    vehiculo             = models.ForeignKey('Vehiculo',  on_delete=models.CASCADE)
    cliente              = models.ForeignKey('Clientes',  on_delete=models.CASCADE)
    fecha_renta          = models.DateField(auto_now=False,auto_now_add=False)
    fecha_devolucion     = models.DateField(auto_now=False,auto_now_add=False)
    monto_dia            = models.PositiveIntegerField(default=0)
    cantidad_dia         = models.PositiveIntegerField(blank=True, null=True)
    comentario           = models.CharField(max_length=100)
    create_at            = models.DateTimeField(auto_now_add=True)
    update_at            = models.DateTimeField(auto_now=True)
    user                 = models.ForeignKey(User)

    def __str__(self):
        return self.cliente.nombre + " | "+str(self.create_at)
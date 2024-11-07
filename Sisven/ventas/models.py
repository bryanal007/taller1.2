from django.db import models
from .models import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre: ', unique = True, blank= False, help_text= 'Ingresa solo texto')

    def _str_(self):
        return self.nombre
    
class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre: ', blank= False)
    precio =  models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Precio: ', blank= False)
    stock = models.IntegerField()
    Categoria= models.ForeignKey(Categoria , on_delete= models.RESTRICT)

    def __str__(self):
        return self.nombre
        
class Cliente(models.Model):
    cedula = models.CharField(max_length=10, verbose_name='Cedula: ', unique= True, blank= False, null= False)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del cliente: ', blank= False)
    apellido = models.CharField(max_length=100, verbose_name='Apellido del cliente: ', blank= False)
    edad = models.IntegerField()
    email = models.EmailField()
    domicilio = models.TextField(max_length=200, help_text='Escribe la referencia de tu domicilio')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
        
class Orden (models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    Producto = models.ManyToManyField(Productos)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        # Utiliza 'self.Cliente' porque así está definido el campo en mayúscula
        return f'Orden de {self.id} - Cliente: {self.Cliente.nombre}'
from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Productos, Orden
admin.site.register (Categoria)
admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Orden)
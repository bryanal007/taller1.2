from django import forms
from .models import Categoria, Productos, Cliente, Orden

# FORMULARIO DE CATEGORIA
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {'nombre': 'Nombre de la categoría'}
        help_texts = {'nombre': 'Ingresa solo texto para el nombre de la categoría'}

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Categoria.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe una categoría con este nombre.")
        return nombre

# FORMULARIO DE PRODUCTOS
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'stock', 'Categoria']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio',
            'stock': 'Cantidad en stock',
            'Categoria': 'Categoría'
        }
        widgets = {
            'precio': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
            'stock': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

# FORMULARIO DE CLIENTE
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'edad', 'email', 'domicilio']
        labels = {
            'cedula': 'Cédula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'email': 'Correo electrónico',
            'domicilio': 'Domicilio'
        }
        widgets = {
            'domicilio': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if not cedula.isdigit() or len(cedula) != 10:
            raise forms.ValidationError("La cédula debe tener exactamente 10 dígitos numéricos.")
        if Cliente.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError("Ya existe un cliente con esta cédula.")
        return cedula

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return edad

# FORMULARIO DE ORDEN
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['Cliente', 'Producto', 'total']
        labels = {
            'Cliente': 'Cliente',
            'Producto': 'Productos',
            'total': 'Total'
        }
        widgets = {
            'Producto': forms.CheckboxSelectMultiple(),
            'total': forms.NumberInput(attrs={'step': 0.01, 'min': 0}),
        }

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total <= 0:
            raise forms.ValidationError("El total debe ser un valor positivo.")
        return total

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto, OrdenForm
@login_required
@permission_required('ventas.view_producto', raise_exception=True)
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/productos.html', {'productos': productos})
@login_required
@permission_required('ventas.add_orden', raise_exception=True)
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
    if form.is_valid():
             form.save()
             return redirect('url_de_exito')  
    else:  
             return render(request, 'ventas/crear_orden.html')
    
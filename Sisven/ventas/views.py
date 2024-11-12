from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Productos, Categoria, Orden, Cliente
from .forms import ProductoForm, CategoriaForm, OrdenForm, ClienteForm

# Vista para listar productos
@login_required
@permission_required('ventas.view_producto', raise_exception=True)
def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'ventas/productos.html', {'productos': productos})

# Vista para editar un producto
@login_required
@permission_required('ventas.change_producto', raise_exception=True)
def editar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)  # Obtén el producto según su id
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)  # Cargar el producto en el formulario
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('listar_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm(instance=producto)  # Cargar el producto en el formulario
    return render(request, 'ventas/editar_producto.html', {'form': form, 'producto': producto})


# Vista para crear un producto
@login_required
@permission_required('ventas.add_producto', raise_exception=True)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'ventas/crear_producto.html', {'form': form})

# Vista para eliminar un producto
@login_required
@permission_required('ventas.delete_producto', raise_exception=True)
def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)  # Obtén el producto por su ID
    if request.method == 'POST':
        producto.delete()  # Elimina el producto
        return redirect('listar_productos')  # Redirige a la lista de productos
    return render(request, 'ventas/eliminar_producto.html', {'producto': producto})

# Vista para editar una orden
@login_required
@permission_required('ventas.change_orden', raise_exception=True)
def editar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)  # Obtén la orden por su ID
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)  # Pasa la instancia de la orden al formulario
        if form.is_valid():
            form.save()  # Guarda la orden editada
            return redirect('listar_ordenes')  # Redirige a la lista de órdenes
    else:
        form = OrdenForm(instance=orden)  # Rellena el formulario con los datos actuales de la orden
    return render(request, 'ventas/editar_orden.html', {'form': form, 'orden': orden})

# Vista para eliminar una orden
@login_required
@permission_required('ventas.delete_orden', raise_exception=True)
def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)  # Obtén la orden por su ID
    if request.method == 'POST':
        orden.delete()  # Elimina la orden
        return redirect('listar_ordenes')  # Redirige a la lista de órdenes
    return render(request, 'ventas/eliminar_orden.html', {'orden': orden})


# Vista para crear una categoría
@login_required
@permission_required('ventas.add_categoria', raise_exception=True)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Cambia el redirect según tu flujo
    else:
        form = CategoriaForm()
    return render(request, 'ventas/crear_categoria.html', {'form': form})

# Vista para crear un cliente
@login_required
@permission_required('ventas.add_cliente', raise_exception=True)
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # Asegúrate de definir una vista para listar clientes
    else:
        form = ClienteForm()
    return render(request, 'ventas/crear_cliente.html', {'form': form})

# Vista para crear una orden
@login_required
@permission_required('ventas.add_orden', raise_exception=True)
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            form.save_m2m()  # Necesario para ManyToMany fields como 'Producto'
            return redirect('listar_ordenes')  # Cambia el redirect según tu flujo
    else:
        form = OrdenForm()
    return render(request, 'ventas/crear_orden.html', {'form': form})

# Vista para listar órdenes
@login_required
@permission_required('ventas.view_orden', raise_exception=True)
def listar_ordenes(request):
    ordenes = Orden.objects.all()  # Asegúrate de que hay alguna lógica para obtener las órdenes
    return render(request, 'ventas/listar_ordenes.html', {'ordenes': ordenes})

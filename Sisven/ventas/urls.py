from django.urls import path
from . import views

urlpatterns = [

     # Ruta para la página principal de ventas
    path('ventas/', views.ventas, name='ventas'),
    
    # Rutas para productos
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # Rutas para categorías
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),

    # Rutas para órdenes
    path('ordenes/', views.listar_ordenes, name='listar_ordenes'),
    path('ordenes/crear/', views.crear_orden, name='crear_orden'),
    path('ordenes/editar/<int:id>/', views.editar_orden, name='editar_orden'),
    path('ordenes/eliminar/<int:id>/', views.eliminar_orden, name='eliminar_orden'),

]

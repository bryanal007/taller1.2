from django import forms
from.models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['Cliente', 'Producto', 'total', 'fecha']
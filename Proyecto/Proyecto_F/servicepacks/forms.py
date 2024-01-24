from django import forms
from . models import Servicepack

class ServicepackForm(forms.ModelForm):
    class Meta:
        model = Servicepack
        fields = "__all__"
        exclude = ['status']
        labels = {
            'image': 'Imagen',
            'name': 'Nombre',
            'decription': 'Descripción',
            'price': 'Precio',                   
        }
        widgets = {
            'image': forms.FileInput(attrs={'placeholder': 'Ingrese la imagen del Paquete'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del Paquete'}),
            'decription': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción del libro'}), 
            'price': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),          
        }
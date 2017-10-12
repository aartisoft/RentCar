from .models import  Marcas
from django import forms

class MarcasForm(forms.Form):
    name = forms.CharField(required=True)

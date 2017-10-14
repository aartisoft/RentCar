from .models import  Marcas, Modelos,TiposCombustibles,TiposVehiculos,Empleados,Clientes,Vehiculo,Rerservaciones
from django import forms
from django.forms import ModelForm

# class MarcasForm(forms.Form):
#     nombre = forms.CharField(required=True, max_length=25)


class MarcasForm(ModelForm):
    class Meta:
        model = Marcas
        exclude = ('updated', 'created','user')

    def __init__(self, *args, **kwargs):
        super(MarcasForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget = forms.TextInput(attrs={
   
            'class':'form-control m-input'})

class ModelosForm(ModelForm):

    class Meta:
        model = Modelos
        exclude = ('updated', 'created','user')

    def __init__(self, *args, **kwargs):


        super(ModelosForm, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['descripcion'].widget = forms.Textarea(attrs={
            'class':'form-control m-input'})

        self.fields['marca'] = forms.ModelChoiceField(queryset=Marcas.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))


class TiposCombustiblesForm(ModelForm):
    class Meta:
        model = TiposCombustibles
        exclude = ('updated', 'created','user')

    def __init__(self, *args, **kwargs):
        super(TiposCombustiblesForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['descripcion'].widget = forms.Textarea(attrs={
            'class':'form-control m-input'})

class TiposVehiculosForm(ModelForm):
    class Meta:
        model = TiposVehiculos
        exclude = ('updated', 'created','user')

    def __init__(self, *args, **kwargs):
        super(TiposVehiculosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
            
        self.fields['descripcion'].widget = forms.Textarea(attrs={
            'class':'form-control m-input'})

class VehiculosForm(ModelForm):
    class Meta:
        model = Vehiculo
        exclude = ('updated', 'created','user')


    def __init__(self, *args, **kwargs):
        
        super(VehiculosForm, self).__init__(*args, **kwargs)


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

        COLOR_CHOICES = (
            ('Azul', 'Azul'),
            ('Verde','Verde'),
            ('Rojo', 'Rojo'),
            ('Amarillo', 'Amarillo'),
            ('Purpura', 'Purpura'),
            ('Negro', 'Negro'),
            ('Blanco', 'Blanco'),
            ('Marron', 'Marron'),
            ('Dorado', 'Dorado'),
            ('Gris', 'Gris'),
            )    

        self.fields['descripcion'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['no_chasis'] = forms.CharField(max_length=15, widget=forms.TextInput(attrs=
            {'class':'form-control m-input'}))
        
        self.fields['no_motor'] = forms.CharField(max_length=15, widget=forms.TextInput(attrs=
            {'class':'form-control m-input'}))

        self.fields['no_placa'] = forms.CharField(max_length=7, widget=forms.TextInput(attrs=
            {'class':'form-control m-input'}))

                
        self.fields['modelo'] = forms.ModelChoiceField(queryset=Modelos.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))

        self.fields['tipo'] = forms.ModelChoiceField(queryset=TiposVehiculos.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))

        self.fields['combustible'] = forms.ModelChoiceField(queryset=TiposCombustibles.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))

        self.fields['anio'].widget = forms.Select(choices=YEAR_CHOICES,attrs={
            'class':'form-control m-input'})

        self.fields['color'].widget = forms.Select(choices=COLOR_CHOICES,attrs={
            'class':'form-control m-input'})

        self.fields['tarifa'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})






class ReservacionesForm(ModelForm):
    class Meta:
        model = Rerservaciones
        exclude = ('updated', 'created','user')


    def __init__(self, *args, **kwargs):
        
        super(ReservacionesForm, self).__init__(*args, **kwargs)


                  
        self.fields['empleado'] = forms.ModelChoiceField(queryset=Empleados.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))

        self.fields['vehiculo'] = forms.ModelChoiceField(queryset=Vehiculo.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))

        self.fields['cliente'] = forms.ModelChoiceField(queryset=Clientes.objects.all(),empty_label=None,widget=forms.Select(attrs={'class':'form-control m-input'}))


        self.fields['fecha_renta'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['fecha_devolucion'] = forms.CharField(max_length=15, widget=forms.TextInput(attrs=
            {'class':'form-control m-input'}))

        self.fields['monto_dia'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})
        

        self.fields['cantidad_dia'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})

        self.fields['comentario'].widget = forms.Textarea(attrs={
            'class':'form-control m-input'})














   
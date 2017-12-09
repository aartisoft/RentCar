from .models import  Marcas, Modelos,TiposCombustibles,TiposVehiculos,Empleados,Clientes,Vehiculo,Rerservaciones
from bootstrap_datepicker.widgets import DatePicker
from .utils import validar_cedula,validar_tarjeta
from django import forms
#from django.core.exceptions import 
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        print(nombre)
        if nombre=="jorge":
            raise forms.ValidationError("El nombre de la marca no puede ser jorge")
        return nombre

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
        form_tag = False

    def __init__(self, *args, **kwargs):
        
        super(VehiculosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


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


        self.fields['fecha_renta'] = forms.DateField(widget=DatePicker(
            attrs={
            'class':'form-control m-input'},
            options={  "format": "mm/dd/yyyy",
                        "autoclose": True
                        }))

        

        self.fields['fecha_devolucion'] = forms.DateField(widget=DatePicker(
            attrs={
            'class':'form-control m-input'},
            options={  "format": "mm/dd/yyyy",
                        "autoclose": True
                        }))

        self.fields['monto_dia'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})
        

        self.fields['cantidad_dia'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})

        self.fields['comentario'].widget = forms.Textarea(attrs={
            'class':'form-control m-input'})



class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        exclude = ('updated', 'created','user')


    def __init__(self, *args, **kwargs):
        
        super(ClientesForm, self).__init__(*args, **kwargs)

        TYPE_PERSON_CHOISES = ( 
            ('Fisica', 'Fisica'), 
            ('Juridica', 'Juridica'),)

        SEX_CHOISES = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),)

        self.fields['nombre'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['cedula'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['no_tjcredito'] = forms.CharField(label="No. de Tarjeta de Credito")
        
        self.fields['no_tjcredito'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['limite_credito'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['tipo_persona'].widget = forms.Select(choices=TYPE_PERSON_CHOISES,attrs={
            'class':'form-control m-input'})

        self.fields['sexo'].widget = forms.Select(choices=SEX_CHOISES,attrs={
            'class':'form-control m-input'})
    
        self.fields['fecha_nacimiento'] = forms.DateField(widget=DatePicker(
            attrs={
            'class':'form-control m-input'},
            options={  "format": "mm/dd/yyyy",
                        "autoclose": True
                        }))

        self.fields['licencia'] = forms.CharField(label="No. de Licencia")
        
        self.fields['licencia'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['direccion'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']

        if "-" in cedula:
            raise forms.ValidationError("No se permiten:-")
            
        if " " in cedula:
            raise forms.ValidationError("No se permiten:-")  

        if cedula:
            if len(cedula) !=11:
                raise forms.ValidationError("El numero de cedula debe de tener 11 digitos")  
     
        if validar_cedula(cedula)==False:
            raise forms.ValidationError("Este numero de cedula no es valido")

        qs = Clientes.objects.filter(cedula__contains=cedula)
        if qs.exists():
            raise forms.ValidationError("Ya existe un cliente con esta cedula")


        return cedula.replace('-','')

    
    def clean_no_tjcredito(self):
        no_tjcredito = self.cleaned_data['no_tjcredito']
     
        if validar_tarjeta(no_tjcredito)==False:
            raise forms.ValidationError("La tarjeta no esta correcta")

        return no_tjcredito
                  
                  
      





class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        exclude = ('updated', 'created','user')


    def __init__(self, *args, **kwargs):
        
        super(EmpleadosForm, self).__init__(*args, **kwargs)


        self.fields['nombre'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['cedula'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})
                
        self.fields['telefono'].widget = forms.TextInput(attrs={
            'class':'form-control m-input'})

        self.fields['comision'].widget = forms.NumberInput(attrs={
            'class':'form-control m-input'})
        
        self.fields['fecha_nacimiento'] = forms.DateField(widget=DatePicker(
            attrs={
            'class':'form-control m-input'},
            options={  "format": "mm/dd/yyyy",
                        "autoclose": True
                        }))

        self.fields['fecha_ingreso'] = forms.DateField(widget=DatePicker(
            attrs={
            'class':'form-control m-input'},
            options={  "format": "mm/dd/yyyy",
                        "autoclose": True
                        }))


    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        print(cedula)
     
        if validar_cedula(cedula)==False:
            raise forms.ValidationError("La cedula esta incorrecta")

        qs = Empleados.objects.filter(cedula__contains=cedula)
        if qs.exists():
            raise forms.ValidationError("Ya existe un empleado con esta cedula")


        return cedula
                  
      






   
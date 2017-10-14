
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Marcas,Modelos,TiposCombustibles,TiposVehiculos,Vehiculo,Clientes,Empleados,Rerservaciones
from .forms import MarcasForm, ModelosForm,TiposCombustiblesForm,TiposVehiculosForm,VehiculosForm,ReservacionesForm
from django.db.models.signals import pre_save
#from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
import django_tables2 as tables

# Create your views here.

class MarcarTable(tables.Table):
    id = tables.Column()
    nombre = tables.Column()
    

    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def MarcasViewTable(request):
    table =MarcarTable(Marcas.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'marcas/list.html', {'marcas': table})

class MarcasCreateView(LoginRequiredMixin,CreateView):
    model=Marcas
    fields = ['nombre']
    template_name = 'marcas/create.html'
    success_url = '/marcas/'
    # login_url = '/login/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user=self.request.user
        
        return super(MarcasCreateView, self).form_valid(form) # Call the real save() method


@login_required
def form_marca_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MarcasForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj = Marcas.objects.create(nombre=form.cleaned_data.get('nombre'),
                                        user=request.user)

            return HttpResponseRedirect('/marcas/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MarcasForm()

    return render(request, 'marcas/create.html', {'form': form})

@login_required
def form_modelo_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj = Modelos.objects.create(nombre=form.cleaned_data.get('nombre'),
                                        descripcion=form.cleaned_data.get('descripcion'),
                                        marca=form.cleaned_data.get('marca'),
                                        user=request.user)

            return HttpResponseRedirect('/modelos/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelosForm()

    return render(request, 'modelos/create.html', {'form': form})


@login_required
def form_tiposcombustibles_view(request):

    if request.method == 'POST':
 
        form = TiposCombustiblesForm(request.POST)
 
        if form.is_valid():
    
            obj = TiposCombustibles.objects.create( nombre=form.cleaned_data.get('nombre'),
                                                    descripcion=form.cleaned_data.get('descripcion'),
                                                    user=request.user)

            return HttpResponseRedirect('/tiposcombustibles/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TiposCombustiblesForm()

    return render(request, 'tiposcombustibles/create.html', {'form': form})


@login_required
def form_tiposvehiculos_view(request):

    if request.method == 'POST':
    
        form = TiposVehiculosForm(request.POST)

        if form.is_valid():

            obj = TiposVehiculos.objects.create( nombre=form.cleaned_data.get('nombre'),
                                                    descripcion=form.cleaned_data.get('descripcion'),
                                                    user=request.user)

            return HttpResponseRedirect('/tiposvehiculos/')
    else:
        form = TiposVehiculosForm()

    return render(request, 'tiposvehiculos/create.html', {'form': form})

@login_required
def form_vehiculos_view(request):

    if request.method == 'POST':
    
        form = VehiculosForm(request.POST)

        if form.is_valid():

            obj = Vehiculo.objects.create(   descripcion = form.cleaned_data.get('descripcion'),
                                             no_chasis = form.cleaned_data.get('no_chasis'),
                                             no_motor = form.cleaned_data.get('no_chasis'),
                                             no_placa = form.cleaned_data.get('no_chasis'),
                                             modelo = form.cleaned_data.get('modelo'),
                                             tipo = form.cleaned_data.get('tipo'),
                                             combustible = form.cleaned_data.get('combustible'),
                                             anio = form.cleaned_data.get('anio'),
                                             color = form.cleaned_data.get('color'),
                                             tarifa = form.cleaned_data.get('tarifa'),
                                             user=request.user)

            return HttpResponseRedirect('/vehiculos/')
    else:
        form = VehiculosForm()

    return render(request, 'vehiculos/create.html', {'form': form})


@login_required
def form_reservaciones_view(request):

    if request.method == 'POST':
    
        form = ReservacionesForm(request.POST)

        if form.is_valid():

            obj = Rerservaciones.objects.create(  empleado = form.cleaned_data.get('empleado'),
                                             vehiculo = form.cleaned_data.get('vehiculo'),
                                             cliente = form.cleaned_data.get('cliente'),
                                             fecha_renta = form.cleaned_data.get('fecha_renta'),
                                             fecha_devolucion = form.cleaned_data.get('fecha_devolucion'),
                                             monto_dia = form.cleaned_data.get('monto_dia'),
                                             cantidad_dia = form.cleaned_data.get('cantidad_dia'),
                                             comentario = form.cleaned_data.get('comentario'),
                                             user=request.user)

            return HttpResponseRedirect('/reservaciones/')
    else:
        form = ReservacionesForm()

    return render(request, 'reservaciones/create.html', {'form': form})






class  ModeloTable(tables.Table):
    id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column()
    marca = tables.Column()
    

    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def ModelosViewTable(request):
    table = ModeloTable(Modelos.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'modelos/list.html', {'table': table})

class ModelosCreateView(LoginRequiredMixin,CreateView):
    model= Modelos
    fields = ['nombre','descripcion','marca']
    template_name = 'modelos/create.html'
    success_url = '/modelos/'
    # login_url = '/login/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ModelosCreateView, self).form_valid(form) # Call the real save() method
        



class  TipoCombustibleTable(tables.Table):
    id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column()


    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def TipoCombustibleViewTable(request):
    table = TipoCombustibleTable(TiposCombustibles.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'tiposcombustibles/list.html', {'table': table})

    


class  TiposCombustiblesCreateView(LoginRequiredMixin,CreateView):
    model= TiposCombustibles
    fields = ['nombre','descripcion']
    template_name = 'tiposcombustibles/create.html'
    success_url = '/tiposcombustibles/'
    # login_url = '/login/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(TiposCombustiblesCreateView, self).form_valid(form) # Call the real save() method



class  TipoVehiculosTable(tables.Table):
    id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column()


    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def TipoVehiculosViewTable(request):
    table = TipoVehiculosTable(TiposVehiculos.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'tiposvehiculos/list.html', {'table': table})

    
class  TiposVehiculosCreateView(LoginRequiredMixin,CreateView):
    model= TiposVehiculos
    fields = ['nombre','descripcion']
    template_name = 'tiposvehiculos/create.html'
    success_url = '/tiposvehiculos/'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(TiposVehiculosCreateView, self).form_valid(form)




class  VehiculosTable(tables.Table):
    id = tables.Column()
    descripcion = tables.Column()
    no_chasis   = tables.Column()
    no_motor    = tables.Column()
    no_placa    = tables.Column()
    modelo      = tables.Column()
    tipo        = tables.Column()
    combustible = tables.Column()
    anio        = tables.Column()
    color       = tables.Column()
    tarifa      = tables.Column()
 


    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def VehiculosViewTable(request):
    table = VehiculosTable(Vehiculo.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'vehiculos/list.html', {'table': table})

    
class  VehiculosCreateView(LoginRequiredMixin,CreateView):
    model= Vehiculo
    fields = ['descripcion','no_chasis','no_motor','no_placa','modelo','tipo','combustible','anio','color','tarifa']
    template_name = 'vehiculos/create.html'
    success_url = '/vehiculos/'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(VehiculosCreateView, self).form_valid(form)



class  ClientesTable(tables.Table):
    id                      = tables.Column()
    nombre                  = tables.Column()
    cedula                  = tables.Column()
    no_tjcredito            = tables.Column(accessor='No_Tarjecta_Credito')
    limite_credito          = tables.Column()
    tipo_persona            = tables.Column()
    sexo                    = tables.Column()
    fecha_nacimiento        = tables.Column()
    licencia = tables.Column()
  
    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def ClientesViewTable(request):
    table = ClientesTable(Clientes.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'clientes/list.html', {'table': table})

    
class  ClientesCreateView(LoginRequiredMixin,CreateView):
    model= Clientes
    fields = ['nombre','cedula','no_tjcredito','limite_credito','tipo_persona','sexo','fecha_nacimiento','licencia','direccion']
    template_name = 'clientes/create.html'
    success_url = '/clientes/'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ClientesCreateView, self).form_valid(form)


class  EmpleadosTable(tables.Table):
    id = tables.Column()
    nombre = tables.Column()
    cedula   = tables.Column()
    telefono    = tables.Column()
    comision    = tables.Column()
    fecha_nacimiento       = tables.Column()
    fecha_ingreso                = tables.Column()

  
    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def EmpleadosViewTable(request):
    table = EmpleadosTable(Empleados.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'empleados/list.html', {'table': table})

    
class EmpleadosCreateView(LoginRequiredMixin,CreateView):
    model= Empleados
    fields = ['nombre','cedula','telefono','comision','fecha_nacimiento','fecha_ingreso']
    template_name = 'empleados/create.html'
    success_url = '/empleados/'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(EmpleadosCreateView, self).form_valid(form)



class  ReservacionesTable(tables.Table):
    id = tables.Column()
    empleado = tables.Column()
    vehiculo   = tables.Column()
    cliente    = tables.Column()
    fecha_renta    = tables.Column()
    fecha_devolucion       = tables.Column()
    monto_dia                = tables.Column()
    cantidad_dia       = tables.Column()
    comentario                = tables.Column()

    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def ReservacionesViewTable(request):
    table = ReservacionesTable(Rerservaciones.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'reservaciones/list.html', {'table': table})

    
class ReservacionesCreateView(LoginRequiredMixin,CreateView):
    model= Rerservaciones
    fields = ['empleado','vehiculo','cliente','fecha_renta','fecha_devolucion','monto_dia','cantidad_dia','comentario']
    template_name = 'reservaciones/create.html'
    success_url = '/reservaciones/'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ReservacionesCreateView, self).form_valid(form)



# @receiver(pre_save, sender=Marcas)
#     def my_handler(sender, **kwargs):



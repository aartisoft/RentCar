
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from .models import Marcas,Modelos,TiposCombustibles,TiposVehiculos,Vehiculo,Clientes,Empleados,Rerservaciones
from .forms import MarcasForm, ModelosForm,TiposCombustiblesForm,TiposVehiculosForm,VehiculosForm,ReservacionesForm
from .forms import ClientesForm,EmpleadosForm
from django.db.models.signals import pre_save
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django_tables2.utils import A
from django.urls import reverse_lazy
# from django_filters import FilterView
import django_filters
from django_tables2.views import SingleTableMixin
import django_tables2 as tables
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter




# Create your views here.

class MarcarTable(tables.Table):
    #id = tables.Column()
    nombre = tables.Column()
    pk = tables.LinkColumn('marca-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('marca-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    

    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def MarcasViewTable(request):
    table = MarcarTable(Marcas.objects.all())

    table.order_by = 'create_at'

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

@login_required
def form_clientes_view(request):

    if request.method == 'POST':
    
        form = ClientesForm(request.POST)

        if form.is_valid():

            obj = Clientes.objects.create(   nombre = form.cleaned_data.get('nombre'),
                                             cedula = form.cleaned_data.get('cedula'),
                                             no_tjcredito = form.cleaned_data.get('no_tjcredito'),
                                             limite_credito = form.cleaned_data.get('limite_credito'),
                                             tipo_persona = form.cleaned_data.get('tipo_persona'),
                                             sexo = form.cleaned_data.get('sexo'),
                                             fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento'),
                                             licencia = form.cleaned_data.get('licencia'),
                                             direccion = form.cleaned_data.get('direccion'),
                                             user=request.user)

            return HttpResponseRedirect('/clientes/')
    else:

        form = ClientesForm()

    return render(request, 'clientes/create.html', {'form': form})

@login_required
def form_empleados_view(request):

    if request.method == 'POST':
    
        form = EmpleadosForm(request.POST)

        if form.is_valid():

            obj = Empleados.objects.create(  nombre = form.cleaned_data.get('nombre'),
                                             cedula = form.cleaned_data.get('cedula'),
                                             telefono = form.cleaned_data.get('telefono'),
                                             comision = form.cleaned_data.get('comision'),
                                             fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento'),
                                             fecha_ingreso = form.cleaned_data.get('fecha_ingreso'),
                                             user=request.user)

            return HttpResponseRedirect('/empleados/')
    else:

        form = EmpleadosForm()

    return render(request, 'empleados/create.html', {'form': form})



class  ModeloTable(tables.Table):
    # id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column(empty_values=())
    marca = tables.Column()
    pk = tables.LinkColumn('modelo-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('modelo-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    

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
    # id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column(empty_values=())
    pk = tables.LinkColumn('tipocombustible-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('tipocombustible-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    


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
    # id = tables.Column()
    nombre = tables.Column()
    descripcion = tables.Column(empty_values=())
    pk = tables.LinkColumn('tipovehiculo-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('tipovehiculo-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    


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
    # id = tables.Column()
    descripcion = tables.Column()
    no_chasis   = tables.Column(verbose_name='No. Chasis')
    no_motor    = tables.Column(verbose_name='No. Motor')
    no_placa    = tables.Column(verbose_name='No. Plca')
    modelo      = tables.Column()
    tipo        = tables.Column()
    combustible = tables.Column()
    anio        = tables.Column()
    color       = tables.Column()
    tarifa      = tables.Column()
    pk = tables.LinkColumn('vehiculo-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('vehiculo-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    

 


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
    no_tjcredito            = tables.Column(verbose_name='No. Tarjeta  de Credito')
    limite_credito          = tables.Column(verbose_name='Limite de Credito')
    tipo_persona            = tables.Column()
    sexo                    = tables.Column()
    fecha_nacimiento        = tables.Column()
    licencia                = tables.Column(verbose_name='No. de Licencia')
    pk = tables.LinkColumn('cliente-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('cliente-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    

  
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
    pk = tables.LinkColumn('empleado-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('empleado-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    
  
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
    # id = tables.Column()
    empleado = tables.Column()
    vehiculo   = tables.Column()
    cliente    = tables.Column()
    fecha_renta    = tables.Column()
    fecha_devolucion       = tables.Column()
    monto_dia                = tables.Column()
    cantidad_dia       = tables.Column()
    comentario                = tables.Column()
    pk = tables.LinkColumn('reservacion-update',verbose_name='Editar',args=[A('pk')], text='',attrs={'a':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-accent  m-btn--icon-only m-btn--pill flaticon-interface-3','title': 'Editar'}})
    id = tables.LinkColumn('reservacion-delete',verbose_name='Eliminar',args=[A('id')], text='',attrs={'td':{'class': 'm-portlet__nav-link btn m-btn m-btn--hover-danger  m-btn--icon-only m-btn--pill flaticon-circle','title': 'Eliminar' }})
    
    

    class Meta:
        attrs = {'class': 'table table-striped table-bordered'}
 
def ReservacionesViewTable(request):
    table = ReservacionesTable(Rerservaciones.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'reservaciones/list.html', {'table': table})

    
class ReservacionesCreateView(LoginRequiredMixin, CreateView):
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

class MarcasUpdateView(UpdateView,FormMixin):
    model = Marcas
    # fields = ['nombre']
    #template_name_suffix = '_update_form'
    form_class = MarcasForm
    template_name= 'marcas/create.html'
    success_url = '/marcas/'
    
class MarcasDeleteView(DeleteView):
    model = Marcas
    success_url = '/marcas/'
    template_name= 'marcas/delete.html'



class ModelosUpdateView(UpdateView,FormMixin):
    model = Modelos
    # fields = ['nombre']
    #template_name_suffix = '_update_form'
    form_class = ModelosForm
    template_name= 'modelos/create.html'
    success_url = '/modelos/'
    
class ModelosDeleteView(DeleteView):
    model = Modelos
    success_url = '/modelos/'
    template_name= 'modelos/delete.html'

class TiposCombustiblesUpdateView(UpdateView,FormMixin):
    model = TiposCombustibles
    # fields = ['nombre']
    #template_name_suffix = '_update_form'
    form_class = TiposCombustiblesForm
    template_name= 'tiposcombustibles/create.html'
    success_url = '/tiposcombustibles/'
    
class TiposCombustiblesDeleteView(DeleteView):
    model = TiposCombustibles
    success_url = '/tiposcombustibles/'
    template_name= 'tiposcombustibles/delete.html'


class TiposVehiculosUpdateView(UpdateView,FormMixin):
    model = TiposVehiculos
    form_class = TiposVehiculosForm
    template_name= 'tiposvehiculos/create.html'
    success_url = '/tiposvehiculos/'
    
class TiposVehiculosDeleteView(DeleteView):
    model = TiposVehiculos
    success_url = '/tiposvehiculos/'
    template_name= 'tiposvehiculos/delete.html'

class VehiculosUpdateView(UpdateView,FormMixin):
    model = Vehiculo
    form_class = VehiculosForm
    template_name= 'vehiculos/create.html'
    success_url = '/vehiculos/'
    
class VehiculosDeleteView(DeleteView):
    model = TiposVehiculos
    success_url = '/vehiculos/'
    template_name= 'vehiculos/delete.html'

class RerservacionesUpdateView(UpdateView,FormMixin):
    model = Rerservaciones
    form_class = ReservacionesForm
    template_name= 'reservaciones/create.html'
    success_url = '/reservaciones/'
    
class RerservacionesDeleteView(DeleteView):
    model = Rerservaciones
    success_url = '/reservaciones/'
    template_name= 'reservaciones/delete.html'
    

class ClientesUpdateView(UpdateView,FormMixin):
    model = Clientes
    form_class = ClientesForm
    template_name= 'clientes/create.html'
    success_url = '/clientes/'
    
class ClientesDeleteView(DeleteView):
    model = Clientes
    success_url = '/clientes/'
    template_name= 'clientes/delete.html'
    

class EmpleadosUpdateView(UpdateView,FormMixin):
    model = Empleados
    form_class = EmpleadosForm
    template_name= 'empleados/create.html'
    success_url = '/empleados/'
    
class EmpleadosDeleteView(DeleteView):
    model = Empleados
    success_url = '/empleados/'
    template_name= 'empleados/delete.html'
    


def testViewTableJson(request):

    data =  json.loads({"nombre":"Lucia"})

    print(json.dumps(data))
    return JsonResponse(json.dumps(data))



class VehiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Vehiculo
        fields = ['modelo']

class FilteredVehiculoListView(SingleTableMixin):
    table_class = VehiculosTable
    model = Vehiculo
    template_name = 'vehiculos/test_list.html'
    filterset_class = VehiculoFilter



def print_marcas(request):
    buffer = BytesIO()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="marcas.pdf"'

    doc = SimpleDocTemplate(buffer,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=72)

    # Our container for 'Flowable' objects
    elements = []

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='LeftAlign', alignment=TA_RIGHT))

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    marcas = Marcas.objects.all()
    elements.append(Paragraph('Marcas', styles['LeftAlign']))

    # Need a place to store our table rows
    table_data = []
    for i, marca in enumerate(marcas):
        # Add a row to the table
        table_data.append([marca.nombre])
    # Create the table
    user_table = Table(table_data, colWidths=[doc.width/3.0]*3)
    user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    elements.append(user_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def print_clientes(request):
    buffer = BytesIO()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clientes.pdf"'

    doc = SimpleDocTemplate(buffer,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=72)

    # Our container for 'Flowable' objects
    elements = []

    # A large collection of style sheets pre-made for us
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='LeftAlign', alignment=TA_RIGHT))

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    list_objects = Clientes.objects.all()
    elements.append(Paragraph('Clientes', styles['LeftAlign']))

    # Need a place to store our table rows
    table_data = []
    for i, item in enumerate(list_objects):
        # Add a row to the table
        table_data.append([item.nombre,item.cedula,item.no_tjcredito,item.tipo_persona])
    # Create the table
    user_table = Table(table_data, colWidths=[doc.width/3.0])
    user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    elements.append(user_table)
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def generar_pdf_clientes(request):
    print ("Genero el PDF")
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Clientes", styles['Heading2'])
    clientes.append(header)
    linea = Paragraph("_________________________________________________________________", styles['Heading2'])
    clientes.append(linea)
    headings = ('Nombre', 'Cedula', 'No. Credito', 'Tipo Persona','Sexo','Fecha Nacimiento')
    allclientes = [(p.nombre, p.cedula, p.no_tjcredito, p.tipo_persona, p.sexo, p.fecha_nacimiento) for p in Clientes.objects.all()]
    print (allclientes)

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (5, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.gray)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response


def generar_pdf_modelos(request):
    print ("Genero el PDF")
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "modelos.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Modelos de Vehiculos", styles['Heading2'])
    clientes.append(header)
    linea = Paragraph("_________________________________________________________________", styles['Heading2'])
    clientes.append(linea)
    headings = ('Nombre                                    ', 'Descripcion                                    ', 'Marca                                    ')
    allclientes = [(p.nombre, p.descripcion, p.marca.nombre) for p in Modelos.objects.all()]
    print (allclientes)

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.gray),
            
        
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response




def generar_pdf_marcas(request):
    print ("Genero el PDF")
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "marcas.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Marcas de Vehiculos", styles['Heading2'])
    clientes.append(header)
    linea = Paragraph("_________________________________________________________________", styles['Heading2'])
    clientes.append(linea)
    headings = ('Nombre ')
    allmarcas = [(p.nombre) for p in Marcas.objects.all()]
    print (allmarcas)

    t = Table([headings] + allmarcas)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (2, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.gray)
            
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response

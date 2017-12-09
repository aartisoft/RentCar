"""rentcar_easy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.generic import TemplateView
from rentcar.views import MarcasViewTable,MarcasCreateView,ModelosViewTable,ModelosCreateView,TipoCombustibleViewTable
from rentcar.views import TiposCombustiblesCreateView, TipoVehiculosViewTable,TiposVehiculosCreateView,  VehiculosViewTable,VehiculosCreateView
from rentcar.views import ClientesViewTable,ClientesCreateView,EmpleadosViewTable,EmpleadosCreateView,ReservacionesViewTable,ReservacionesCreateView
from rentcar.views import form_marca_view, form_modelo_view,form_tiposcombustibles_view,form_tiposvehiculos_view,form_vehiculos_view,form_reservaciones_view
from rentcar.views import form_clientes_view,form_empleados_view, testViewTableJson, MarcasUpdateView,MarcasDeleteView, VehiculosUpdateView, VehiculosDeleteView
from rentcar.views import ModelosUpdateView,ModelosDeleteView,TiposCombustiblesUpdateView,TiposCombustiblesDeleteView,TiposVehiculosUpdateView,TiposVehiculosDeleteView
from rentcar.views import RerservacionesUpdateView, RerservacionesDeleteView, ClientesUpdateView, ClientesDeleteView, EmpleadosUpdateView, EmpleadosDeleteView
from rentcar.views import FilteredVehiculoListView,print_marcas, generar_pdf_marcas,generar_pdf_clientes, generar_pdf_modelos, generar_pdf_vehiculos,generar_pdf_tiposvehiculos,generar_pdf_tiposcombustibles,generar_pdf_empleados
from rentcar.views import FilteredMarcasListView, FilteredModelosListView, FilteredTiposCombustiblesListView, FilteredTiposVehiculosListView,FilteredClientesListView, FilteredReservacionesListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
# from djurl import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="base/index.html")),
    url(r'^test/table',testViewTableJson),
    url(r'^marcas/$',FilteredMarcasListView.as_view(), name="marcas_table"),
    url(r'^marcas/create/$',form_marca_view),
    url(r'^marcas/update/(?P<pk>[0-9]+)$', MarcasUpdateView.as_view(), name ="marca-update"),
    url(r'^marcas/delete/(?P<pk>[0-9]+)$', MarcasDeleteView.as_view(), name ="marca-delete"),
    url(r'^marcas/report/$',generar_pdf_marcas),
    url(r'^modelos/$',FilteredModelosListView.as_view(), name="modelo_table"),
    url(r'^modelos/create/$',form_modelo_view),
    url(r'^modelos/update/(?P<pk>[0-9]+)$', ModelosUpdateView.as_view(), name ="modelo-update"),
    url(r'^modelos/delete/(?P<pk>[0-9]+)$', ModelosDeleteView.as_view(), name ="modelo-delete"),
    url(r'^modelos/report/$',generar_pdf_modelos),
    url(r'^tiposcombustibles/$',FilteredTiposCombustiblesListView.as_view(), name="tiposcombustibles_table"),
    url(r'^tiposcombustibles/create/$',form_tiposcombustibles_view),
    url(r'^tiposcombustibles/update/(?P<pk>[0-9]+)$', TiposCombustiblesUpdateView.as_view(), name ="tipocombustible-update"),
    url(r'^tiposcombustibles/delete/(?P<pk>[0-9]+)$', TiposCombustiblesDeleteView.as_view(), name ="tipocombustible-delete"),
    url(r'^tiposcombustibles/report/$',generar_pdf_tiposcombustibles),
    url(r'^tiposvehiculos/$',FilteredTiposVehiculosListView.as_view(), name="tiposvehiculos_table"),
    url(r'^tiposvehiculos/create/$',form_tiposvehiculos_view),
    url(r'^tiposvehiculos/update/(?P<pk>[0-9]+)$', TiposVehiculosUpdateView.as_view(), name ="tipovehiculo-update"),
    url(r'^tiposvehiculos/delete/(?P<pk>[0-9]+)$', TiposVehiculosDeleteView.as_view(), name ="tipovehiculo-delete"),
    url(r'^tiposvehiculos/report/$',generar_pdf_tiposvehiculos),
    url(r'^vehiculos/$',FilteredVehiculoListView.as_view(), name="vehiculo_table"),
    url(r'^vehiculos/create/$',form_vehiculos_view),
    url(r'^vehiculos/update/(?P<pk>[0-9]+)$', VehiculosUpdateView.as_view(), name ="vehiculo-update"),
    url(r'^vehiculos/delete/(?P<pk>[0-9]+)$', VehiculosDeleteView.as_view(), name ="vehiculo-delete"),
    url(r'^vehiculos/report/$',generar_pdf_vehiculos),
    url(r'^clientes/$',FilteredClientesListView.as_view(), name="clientes_table"),
    url(r'^clientes/create/$',form_clientes_view),
    url(r'^clientes/update/(?P<pk>[0-9]+)$', ClientesUpdateView.as_view(), name ="cliente-update"),
    url(r'^clientes/delete/(?P<pk>[0-9]+)$', ClientesDeleteView.as_view(), name ="cliente-delete"),
    url(r'^clientes/report/$',generar_pdf_clientes),
    url(r'^empleados/$',EmpleadosViewTable),
    url(r'^empleados/create/$',form_empleados_view),
    url(r'^empleados/update/(?P<pk>[0-9]+)$', EmpleadosUpdateView.as_view(), name ="empleado-update"),
    url(r'^empleados/delete/(?P<pk>[0-9]+)$', EmpleadosDeleteView.as_view(), name ="empleado-delete"),
    url(r'^empleados/report/$',generar_pdf_empleados),
    url(r'^reservaciones/$',FilteredReservacionesListView.as_view(), name="reservaciones_table"),
    url(r'^reservaciones/create/$',form_reservaciones_view),
    url(r'^reservaciones/update/(?P<pk>[0-9]+)$', RerservacionesUpdateView.as_view(), name ="reservacion-update"),
    url(r'^reservaciones/delete/(?P<pk>[0-9]+)$', RerservacionesDeleteView.as_view(), name ="reservacion-delete"),
    url(r'^login/$', LoginView.as_view(),name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

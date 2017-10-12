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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="base/index.html")),
    url(r'^marcas/$',MarcasViewTable),
    url(r'^marcas/create/$',MarcasCreateView.as_view()),
    url(r'^modelos/$',ModelosViewTable),
    url(r'^modelos/create/$',ModelosCreateView.as_view()),
    url(r'^tiposcombustibles/$',TipoCombustibleViewTable),
    url(r'^tiposcombustibles/create/$',TiposCombustiblesCreateView.as_view()),
    url(r'^tiposvehiculos/$',TipoVehiculosViewTable),
    url(r'^tiposvehiculos/create/$',TiposVehiculosCreateView.as_view()),
    url(r'^vehiculos/$',VehiculosViewTable),
    url(r'^vehiculos/create/$',VehiculosCreateView.as_view()),
    url(r'^clientes/$',ClientesViewTable),
    url(r'^clientes/create/$',ClientesCreateView.as_view()),
    url(r'^empleados/$',EmpleadosViewTable),
    url(r'^empleados/create/$',EmpleadosCreateView.as_view()),
    url(r'^reservaciones/$',ReservacionesViewTable),
    url(r'^reservaciones/create/$',ReservacionesCreateView.as_view()),
    url(r'^login/$', LoginView.as_view(),name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

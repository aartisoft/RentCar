import django_filters
from .models import Marcas


class MarcaFilter(django_filters.FilterSet):
    class Meta:
        model = Marcas
        fields = ['nombre']

import django_filters
from .models import *


class ProyectoFilter(django_filters.FilterSet):
	sector = django_filters.CharFilter(name='sector__slug_sector')
	unidad = django_filters.CharFilter(name='unidad__slug_unidad')
	ano = django_filters.CharFilter(name='ano__slug_ano')

	class Meta:
		model = Proyecto
		fields =('sector','unidad','ano')
from django.shortcuts import render
from .models import *
from .serializers import ProyectoSerializer, UserSerializer
from rest_framework import viewsets,  permissions
from django.contrib.auth.models import User
# from rest_framework.decorators import detail_route, action
import django_filters
# from django_filters import DjangoFilterBackend
# from rest_framework_chain import ChainedFilterSet, RelatedFilter
from rest_framework import filters
from prueba_uno.filters import ProyectoFilter


class ProyectoViewSet(viewsets.ModelViewSet):
	model=Proyecto
	
	serializer_class = ProyectoSerializer
	permission_classes= (permissions.IsAuthenticatedOrReadOnly,)
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = ProyectoFilter

class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class = UserSerializer
	permission_classes= (permissions.IsAuthenticatedOrReadOnly,)
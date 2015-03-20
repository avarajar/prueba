from rest_framework import serializers
from .models import *
from .models import *
from django.contrib.auth.models import User
from django.conf import settings


class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Proyecto
		fields =('id','nombre','a_inicial','sector')
		depth= 1

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email')
from django.conf.urls import patterns, include, url
from prueba_uno.models import *
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from prueba_uno.views import ProyectoViewSet, UserViewSet
# from django.contrib.gis.geos import GEOSGeometry, GEOSException
# from wq.db.rest import app

router = routers.DefaultRouter()

router.register(r'proyectos',ProyectoViewSet)

router.register(r'user',UserViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^api-prueba/', include(router.urls)),
    url(r'^api-prueba-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

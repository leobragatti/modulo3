from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .views import HoraView
from .models import Pizza, Cliente

urlpatterns = patterns('',  
    #url(r'hora$', hora_atual, name='hora'),
    url(r'hora$', HoraView.as_view(), name='hora'),
    #url(r'pizzas$', pizzas_pendentes, name='pizzas_pendentes'),
    url(r'pizza$', ListView.as_view(model=Pizza,
									context_object_name='lista')),
    url(r'cliente$', ListView.as_view(model=Cliente,
									context_object_name='lista')),
	url(r'cliente/(\d+)$', ListView.as_view(model=Cliente,
									context_object_name='lista')),
)
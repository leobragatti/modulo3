# coding: utf-8

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

import datetime

from .models import Pizza, Pedido
from .forms import ClienteModelForm

def hora_atual_na_unha(request):
	agora = datetime.datetime.now()
	html = '<html><body><h1>Hora Atual: {0}</h1></body></html>'.format(agora)
	return HttpResponse(html)

class HoraView(TemplateView):
	template_name = 'entrega/hora.html'
	
	def get_context_data(self, **kwargs):
		context = super(HoraView, self).get_context_data(**kwargs)
		context['hora_certa'] = datetime.datetime.now
		return context

def cadastro(request):
	if request.method == 'POST':
		formulario = ClienteModelForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect(reverse('lista-clientes'))
	else:
		formulario = ClienteModelForm()
		
	return render(request, 'entrega/cadastro.html',
				  {'formulario': formulario}
				  )

def pedido_pronto(request):
	if request.method == 'POST':
		pedido_id = request.POST.get('pedido_id')
		pedido = Pedido.objects.get(pk=pedido_id)
		pedido.pronto = True
		pedido.save()
	return HttpResponseRedirect(reverse('lista-pizzas'))
	

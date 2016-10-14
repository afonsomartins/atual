from django.shortcuts import render
from django.http import HttpResponse
from atavirtual.models import CargaHoraria 
from atavirtual.forms import atividadeForm
from cadastro.models import User
from datetime import datetime, timedelta

def horario(request):
	user = User.objects.get(id=request.user.id)
	data = {}
	data['form'] = atividadeForm
	data['saida'] = 'Ata Virtual da EJECT'
	data['lista_entrada_saida'] = CargaHoraria.objects.all().order_by('-id')
    
	form = atividadeForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			atividade = form.cleaned_data["atividade"]
			horario = CargaHoraria()
			horario.setCargaHoraria(atividade, user)
			horario.save()
	return render(request, 'horario.html', data)


def fechar(request):
	user = User.objects.get(id=request.user.id)
	data = {}
	data['form'] = atividadeForm
	data['saida'] = 'Ata Virtual da EJECT'
	data['lista_entrada_saida'] = CargaHoraria.objects.all().order_by('-id')[:1]
    
	form = atividadeForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			atividade = form.cleaned_data["atividade"]
			horario = CargaHoraria()
			horario.setCargaHoraria(atividade, user)
			horario.save()
	return render(request, 'fechamento.html', data)

def sair(request):
	user = User.objects.get(id=request.user.id)
	data = {}
	data['form'] = atividadeForm
	data['saida'] = 'Ata Virtual da EJECT'
	data['lista_entrada_saida'] = CargaHoraria.objects.all().order_by('-id')
    
	form = atividadeForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			atividade = form.cleaned_data["atividade"]
			horario = CargaHoraria()
			horario.setCargaHoraria(atividade, user)
			horario.save()

	return render(request, 'saida.html',data)
	

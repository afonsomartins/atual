from django.db import models
from datetime import datetime, timedelta

class CargaHoraria(models.Model):
	nome = models.CharField(max_length=100)
	cargo = models.CharField(max_length=100)
	atividade = models.TextField()
	entrada_usuario = models.DateTimeField()
	saida_usuario = models.DateTimeField(auto_now_add = False , auto_now = True)

	def setCargaHoraria(self, atividade, user):
		self.atividade = atividade
		self.nome = user.first_name
		self.cargo = user.userinfo.cargo
		self.entrada_usuario = user.last_login
	

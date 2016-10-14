from django.conf.urls import url
from atavirtual.views import *

urlpatterns = [
    url(r'^inicio/$', horario, name='horario'),
    url(r'^inicio/fechar$', fechar, name='fechar'),
    url(r'^inicio/sair$', sair, name='sair'),
    ]
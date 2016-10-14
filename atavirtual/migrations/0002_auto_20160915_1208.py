# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atavirtual', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaHoraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('atividade', models.TextField()),
                ('entrada_usuario', models.DateTimeField()),
                ('saida_usuario', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Carga_Horaria',
        ),
    ]

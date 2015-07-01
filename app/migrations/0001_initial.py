# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Genero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cedula', models.CharField(max_length=10)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Nombres', models.CharField(max_length=50)),
                ('Semestre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Equipo', models.ForeignKey(to='app.Equipo')),
            ],
        ),
    ]

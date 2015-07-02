# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Lugar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Reglamento', models.TextField(null=True, blank=True)),
                ('Costo', models.CharField(max_length=10)),
                ('Numero_Jugadores', models.CharField(max_length=2)),
                ('Campeonato', models.ForeignKey(to='app.Campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Descripcion', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Cedula', models.CharField(max_length=10)),
                ('Foto', models.ImageField(upload_to='PlayerPhotos')),
                ('Nombres', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Equipo', models.ForeignKey(to='app.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Nivel', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='jugador',
            name='Semestre',
            field=models.ForeignKey(to='app.Semestre'),
        ),
        migrations.AddField(
            model_name='escuela',
            name='Facultad',
            field=models.ForeignKey(to='app.Facultad'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='Genero',
            field=models.ForeignKey(to='app.Genero'),
        ),
    ]

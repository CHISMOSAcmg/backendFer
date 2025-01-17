# Generated by Django 5.0.6 on 2024-06-28 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_jefe_proceso_proceso'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jefe_proceso',
            name='proceso',
        ),
        migrations.CreateModel(
            name='Subproceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Queja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(max_length=50)),
                ('proceso', models.ManyToManyField(to='gestion.proceso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subproceso', models.ManyToManyField(to='gestion.subproceso')),
            ],
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('proceso', models.ManyToManyField(to='gestion.proceso')),
                ('subproceso', models.ManyToManyField(to='gestion.subproceso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Caso',
        ),
        migrations.DeleteModel(
            name='Jefe_Proceso',
        ),
    ]

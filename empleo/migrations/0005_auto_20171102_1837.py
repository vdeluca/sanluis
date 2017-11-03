# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleo', '0004_auto_20171101_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puesto',
            name='referencias',
        ),
        migrations.AddField(
            model_name='puesto',
            name='trabajador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleo.Postulante'),
        ),
    ]

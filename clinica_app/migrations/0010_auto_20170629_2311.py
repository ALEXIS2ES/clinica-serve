# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 04:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0009_auto_20170629_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citahistorial',
            old_name='nombree_atencion',
            new_name='nombre_especiali',
        ),
        migrations.RenameField(
            model_name='citahistorial',
            old_name='seri',
            new_name='serie_inscrip',
        ),
    ]

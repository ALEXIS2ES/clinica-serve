# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 02:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0008_auto_20170628_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citainscripcion',
            old_name='apellidos_c',
            new_name='apellidos_clien',
        ),
        migrations.RenameField(
            model_name='citainscripcion',
            old_name='apellidos_o',
            new_name='apellidos_odonto',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0005_auto_20170625_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuentausuario',
            options={'ordering': ['num_cuenta'], 'verbose_name': 'Cuentausuario', 'verbose_name_plural': 'Cuentausuarios'},
        ),
        migrations.RenameField(
            model_name='cuentausuario',
            old_name='usuario',
            new_name='num_cuenta',
        ),
    ]
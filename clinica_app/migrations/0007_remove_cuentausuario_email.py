# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 00:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0006_auto_20170625_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentausuario',
            name='email',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelos',
            old_name='marcar',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='marcar',
            new_name='marca',
        ),
    ]

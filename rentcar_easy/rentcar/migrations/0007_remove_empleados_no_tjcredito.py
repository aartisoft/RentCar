# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0006_auto_20171011_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='no_tjcredito',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0009_auto_20161116_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'permissions': (('can_view_articulo', 'Puede ver el articulo'),)},
        ),
    ]

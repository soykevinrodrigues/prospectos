# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0008_remove_vendedor_targettocall'),
        ('target', '0004_auto_20161102_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='vende',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Vendedor'),
        ),
    ]

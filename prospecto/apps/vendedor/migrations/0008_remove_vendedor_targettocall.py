# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0007_auto_20161116_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='targetToCall',
        ),
    ]

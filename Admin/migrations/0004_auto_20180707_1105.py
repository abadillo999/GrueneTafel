# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-07 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_elevation_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worldborder',
            old_name='geom',
            new_name='mpoly',
        ),
    ]
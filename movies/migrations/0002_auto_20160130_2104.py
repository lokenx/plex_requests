# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='auth_plextoken',
            field=models.CharField(default='abcd1234', max_length=255),
        ),
        migrations.AddField(
            model_name='config',
            name='auth_required',
            field=models.BooleanField(default=False),
        ),
    ]

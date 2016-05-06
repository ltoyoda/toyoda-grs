# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.FloatField(default=1.0, verbose_name=' amplitude (m)')),
                ('s', models.FloatField(default=0.0, verbose_name=' damping coefficient (kg/s)')),
                ('t', models.FloatField(default=6.283032, verbose_name=' frequency (1/s)')),
                ('u', models.FloatField(default=18, verbose_name=' time interval (s)')),
            ],
        ),
    ]

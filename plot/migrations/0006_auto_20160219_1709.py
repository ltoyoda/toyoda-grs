# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0005_auto_20160219_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='f',
            field=models.CharField(default='out-views_2p', max_length=200, verbose_name=' txt filename '),
        ),
    ]

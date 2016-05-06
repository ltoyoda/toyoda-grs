# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0005_auto_20160303_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='A',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='w',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='T',
            new_name='d',
        ),
        migrations.AddField(
            model_name='input',
            name='e',
            field=models.FloatField(verbose_name='Correlation at distance 1000 (m)', default=0.1),
        ),
        migrations.AddField(
            model_name='input',
            name='file',
            field=models.CharField(max_length=200, verbose_name=' file name ', default='first graph'),
        ),
        migrations.AddField(
            model_name='input',
            name='g',
            field=models.FloatField(verbose_name='Correlation at distance 3000 (m)', default=0.1),
        ),
        migrations.AddField(
            model_name='input',
            name='h',
            field=models.FloatField(verbose_name='Correlation at distance 4000 (m)', default=0.0),
        ),
        migrations.AddField(
            model_name='input',
            name='i',
            field=models.FloatField(verbose_name='Correlation at distance 5000 (m)', default=0.0),
        ),
        migrations.AlterField(
            model_name='input',
            name='f',
            field=models.FloatField(verbose_name='Correlation at distance 2000 (m)', default=0.1),
        ),
    ]

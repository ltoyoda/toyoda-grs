# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0007_auto_20160303_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='defo',
            field=models.FloatField(default=0.2, verbose_name=' Maximum deformation (mm)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='a',
            field=models.FloatField(default=0.2, verbose_name=' Maximum deformation (mm)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='b',
            field=models.FloatField(default=0.2, verbose_name=' Correlation at distance 50 (m)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='c',
            field=models.FloatField(default=0.2, verbose_name='Correlation at distance 100 (m)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='d',
            field=models.FloatField(default=0.05, verbose_name='Correlation at distance 500 (m)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='e',
            field=models.FloatField(default=0.05, verbose_name='Correlation at distance 1000 (m)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='f',
            field=models.FloatField(default=0.025, verbose_name='Correlation at distance 2000 (m)'),
        ),
        migrations.AlterField(
            model_name='input',
            name='g',
            field=models.FloatField(default=0.0, verbose_name='Correlation at distance 3000 (m)'),
        ),
    ]

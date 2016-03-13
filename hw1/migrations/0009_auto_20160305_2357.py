# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0008_auto_20160303_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='a',
            field=models.FloatField(verbose_name=' Correlation at distance 100 (m)', default=1),
        ),
        migrations.AlterField(
            model_name='input',
            name='b',
            field=models.FloatField(verbose_name=' Correlation at distance 500 (m)', default=1),
        ),
        migrations.AlterField(
            model_name='input',
            name='c',
            field=models.FloatField(verbose_name='Correlation at distance 1000 (m)', default=1),
        ),
        migrations.AlterField(
            model_name='input',
            name='d',
            field=models.FloatField(verbose_name='Correlation at distance 5000 (m)', default=0.5),
        ),
        migrations.AlterField(
            model_name='input',
            name='defo',
            field=models.FloatField(verbose_name=' What is the maximum deformation expected at the centre of the event (mm)', default=0.2),
        ),
        migrations.AlterField(
            model_name='input',
            name='e',
            field=models.FloatField(verbose_name='Correlation at distance 10000 (m)', default=0.25),
        ),
        migrations.AlterField(
            model_name='input',
            name='f',
            field=models.FloatField(verbose_name='Correlation at distance 15000 (m)', default=0.1),
        ),
        migrations.AlterField(
            model_name='input',
            name='g',
            field=models.FloatField(verbose_name='Correlation at distance 20000 (m)', default=0),
        ),
        migrations.AlterField(
            model_name='input',
            name='h',
            field=models.FloatField(verbose_name='Correlation at distance 25000 (m)', default=0.0),
        ),
        migrations.AlterField(
            model_name='input',
            name='i',
            field=models.FloatField(verbose_name='Correlation at distance 30000 (m)', default=0.0),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0004_auto_20160225_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='A',
            field=models.FloatField(verbose_name=' Maximum deformation (mm)', default=10),
        ),
        migrations.AlterField(
            model_name='input',
            name='T',
            field=models.FloatField(verbose_name='Correlation at distance 500 (m)', default=0.1),
        ),
        migrations.AlterField(
            model_name='input',
            name='b',
            field=models.FloatField(verbose_name=' Correlation at distance 10 (m)', default=1),
        ),
        migrations.AlterField(
            model_name='input',
            name='w',
            field=models.FloatField(verbose_name='Correlation at distance 100 (m)', default=0.5),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0009_auto_20160305_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='c',
            field=models.FloatField(verbose_name='  Correlation at distance 1000 (m)', default=1),
        ),
        migrations.AlterField(
            model_name='input',
            name='d',
            field=models.FloatField(verbose_name='  Correlation at distance 5000 (m)', default=0.5),
        ),
        migrations.AlterField(
            model_name='input',
            name='e',
            field=models.FloatField(verbose_name='  Correlation at distance 10000 (m)', default=0.25),
        ),
    ]

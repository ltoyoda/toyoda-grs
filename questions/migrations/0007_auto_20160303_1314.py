# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0006_auto_20160303_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='a',
            field=models.FloatField(verbose_name=' Maximum deformation (mm)', default=4),
        ),
    ]

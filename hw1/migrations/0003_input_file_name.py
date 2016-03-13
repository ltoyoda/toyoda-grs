# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0002_auto_20160222_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='file_name',
            field=models.CharField(default='first graph', verbose_name=' file name ', max_length=200),
        ),
    ]

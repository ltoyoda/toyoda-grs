# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160212_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.FloatField()),
            ],
        ),
    ]

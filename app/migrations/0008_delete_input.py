# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160215_1651'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Input',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pointofinterest_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
        migrations.DeleteModel(
            name='Zone',
        ),
        migrations.AlterModelOptions(
            name='pointofinterest',
            options={'verbose_name_plural': 'points of interest'},
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
    ]

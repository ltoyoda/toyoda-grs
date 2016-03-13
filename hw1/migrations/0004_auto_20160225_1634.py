# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1', '0003_input_file_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='file_name',
            new_name='f',
        ),
    ]

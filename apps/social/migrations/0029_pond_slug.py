# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0028_auto_20161222_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]

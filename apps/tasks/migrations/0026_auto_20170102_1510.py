# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_auto_20170101_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='milestone',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

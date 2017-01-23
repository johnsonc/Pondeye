# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0034_auto_20161227_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='picture',
            name='last_edited',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='pictureset',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

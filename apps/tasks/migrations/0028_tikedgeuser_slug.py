# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0027_userproject_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='tikedgeuser',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]

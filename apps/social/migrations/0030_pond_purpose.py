# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0029_pond_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond',
            name='purpose',
            field=models.CharField(default=None, max_length=110),
        ),
    ]

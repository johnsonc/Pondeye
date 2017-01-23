# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0030_pond_purpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond',
            name='blurb',
            field=models.CharField(default=None, max_length=15),
        ),
    ]

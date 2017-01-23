# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0032_pondmembership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pond',
            name='blurb',
            field=models.CharField(default=None, max_length=51),
        ),
    ]

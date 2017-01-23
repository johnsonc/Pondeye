# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0039_auto_20170103_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pondmembership',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

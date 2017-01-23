# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0037_auto_20170102_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='pondmembership',
            name='date_removed',
            field=models.DateTimeField(default=None),
        ),
    ]

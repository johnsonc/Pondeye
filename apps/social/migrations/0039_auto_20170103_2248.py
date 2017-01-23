# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0038_pondmembership_date_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='last_edited',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

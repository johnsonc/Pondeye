# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_launchemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Can Only Be View By Specific People'),
        ),
    ]

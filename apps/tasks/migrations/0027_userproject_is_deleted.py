# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_auto_20170102_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_launchemail'),
        ('social', '0031_pond_blurb'),
    ]

    operations = [
        migrations.CreateModel(
            name='PondMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('pond', models.ForeignKey(blank=True, to='social.Pond', null=True)),
                ('user', models.ForeignKey(blank=True, to='tasks.TikedgeUser', null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_launchemail'),
        ('social', '0026_auto_20161126_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_pond', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('pond_creator', models.ForeignKey(related_name='pond_creater', blank=True, to='tasks.TikedgeUser', null=True)),
                ('pond_members', models.ManyToManyField(related_name='pond_member', to='tasks.TikedgeUser')),
            ],
        ),
    ]

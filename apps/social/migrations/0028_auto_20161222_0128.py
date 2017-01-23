# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_launchemail'),
        ('social', '0027_pond'),
    ]

    operations = [
        migrations.CreateModel(
            name='PondRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_response', models.DateTimeField(null=True, blank=True)),
                ('request_accepted', models.BooleanField(default=False)),
                ('request_denied', models.BooleanField(default=False)),
                ('request_responded_to', models.BooleanField(default=False)),
                ('member_that_responded', models.ForeignKey(related_name='the_member_that_responded', blank=True, to='tasks.TikedgeUser', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pond',
            name='tags',
            field=models.ManyToManyField(to='tasks.TagNames'),
        ),
        migrations.AddField(
            model_name='pondrequest',
            name='pond',
            field=models.ForeignKey(blank=True, to='social.Pond', null=True),
        ),
        migrations.AddField(
            model_name='pondrequest',
            name='user',
            field=models.ForeignKey(blank=True, to='tasks.TikedgeUser', null=True),
        ),
    ]

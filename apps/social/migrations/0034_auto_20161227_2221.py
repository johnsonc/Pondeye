# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_userproject_is_public'),
        ('social', '0033_auto_20161224_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PondSpecificProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='graded',
            name='user',
        ),
        migrations.AddField(
            model_name='pond',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Graded',
        ),
        migrations.AddField(
            model_name='pondspecificproject',
            name='pond',
            field=models.ManyToManyField(to='social.Pond'),
        ),
        migrations.AddField(
            model_name='pondspecificproject',
            name='project',
            field=models.ForeignKey(blank=True, to='tasks.UserProject', null=True),
        ),
    ]

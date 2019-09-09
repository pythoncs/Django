# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=100)),
                ('acontent', models.TextField()),
                ('aread', models.IntegerField(default=0)),
                ('apub_datetime', models.DateTimeField(auto_now=True)),
                ('aisDelete', models.BooleanField(default=False)),
            ],
        ),
    ]

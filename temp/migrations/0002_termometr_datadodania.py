# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='termometr',
            name='datadodania',
            field=models.DateField(auto_now_add=True, default=datetime.date(2015, 4, 6)),
            preserve_default=False,
        ),
    ]

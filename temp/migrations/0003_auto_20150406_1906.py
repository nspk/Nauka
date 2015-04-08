# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_termometr_datadodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termometr',
            name='datadodania',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

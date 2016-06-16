# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchlogger', '0002_auto_20160526_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationevent',
            name='tab_id',
            field=models.CharField(default='null', max_length=128),
        ),
    ]

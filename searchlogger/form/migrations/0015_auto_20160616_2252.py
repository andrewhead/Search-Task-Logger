# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0014_auto_20160616_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_preference',
            field=models.IntegerField(blank=True, null=True, verbose_name='Which package would you rather use?', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_quality',
            field=models.IntegerField(blank=True, null=True, verbose_name='Which package has a better community and quality of documentation?', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='postquestionnaire',
            name='likert_perception_change',
            field=models.IntegerField(blank=True, null=True, verbose_name='My perception of the quality of support and documentation for the packages has changed since the first comparison I made.', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20160531_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_community',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=-1, verbose_name='Which package has a better community?'),
        ),
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_documentation',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=-1, verbose_name='Which package has better documentation?'),
        ),
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_preference',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=-1, verbose_name='Which package would you rather use?'),
        ),
        migrations.AlterField(
            model_name='packagecomparison',
            name='likert_quality',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=-1, verbose_name='Which package has a better community and quality of documentation?'),
        ),
        migrations.AlterField(
            model_name='postquestionnaire',
            name='likert_perception_change',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=-1, verbose_name='My perception of the support and documentation for these packages changed over the course of answering these questions.'),
        ),
    ]

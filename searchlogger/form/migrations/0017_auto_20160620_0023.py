# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import form.models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0016_auto_20160620_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagecomparison',
            name='likert_quality',
        ),
        migrations.RemoveField(
            model_name='packagecomparison',
            name='na_likert_quality',
        ),
        migrations.AddField(
            model_name='packagecomparison',
            name='likert_quality_community',
            field=models.IntegerField(blank=True, null=True, verbose_name='Which package has a better community for clients of the package?', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='packagecomparison',
            name='likert_quality_documentation',
            field=models.IntegerField(blank=True, null=True, verbose_name='Which package has better documentation?', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='packagecomparison',
            name='na_likert_quality_community',
            field=form.models.NotApplicableField(default=False, verbose_name="Don't know"),
        ),
        migrations.AddField(
            model_name='packagecomparison',
            name='na_likert_quality_documentation',
            field=form.models.NotApplicableField(default=False, verbose_name="Don't know"),
        ),
        migrations.AlterField(
            model_name='prequestionnaire',
            name='professional_years',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='How many years of experience do you have programming professionally?', choices=[('Less than one year', 'Less than one year'), ('1-2 years', '1-2 years'), ('3-5 years', '3-5 years'), ('6-9 years', '6-9 years'), ('10-19 years', '10-19 years'), ('20 more more years', '20 more more years')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import form.models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_auto_20160606_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagecomparison',
            name='na_likert_preference',
            field=form.models.NotApplicableField(default=False, verbose_name=("N/A / Can't tell",)),
        ),
        migrations.AddField(
            model_name='packagecomparison',
            name='na_likert_quality',
            field=form.models.NotApplicableField(default=False, verbose_name=("N/A / Can't tell",)),
        ),
        migrations.AddField(
            model_name='postquestionnaire',
            name='na_likert_perception_change',
            field=form.models.NotApplicableField(default=False, verbose_name=("N/A / Can't tell",)),
        ),
        migrations.AddField(
            model_name='question',
            name='na_likert_confidence',
            field=form.models.NotApplicableField(default=False, verbose_name=("N/A / Can't tell",)),
        ),
        migrations.AlterField(
            model_name='question',
            name='likert_confidence',
            field=models.IntegerField(blank=True, null=True, verbose_name='How confident are you in your assessment of which is better?', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='na_likert_comparison_evidence',
            field=form.models.NotApplicableField(default=False, verbose_name=("N/A / Can't tell",)),
        ),
    ]

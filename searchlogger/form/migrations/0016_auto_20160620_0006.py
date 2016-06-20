# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0015_auto_20160616_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='prequestionnaire',
            name='coding_reason',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='The main reason I write code is for:...', choices=[('Work', 'Work'), ('Research', 'Research'), ('Hobbies', 'Hobbies'), ('Coursework', 'Coursework')]),
        ),
        migrations.AddField(
            model_name='prequestionnaire',
            name='occupation_other',
            field=models.CharField(max_length=200, null=True, verbose_name="If 'Other', what is your occupation?", blank=True),
        ),
        migrations.AddField(
            model_name='prequestionnaire',
            name='professional_years',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='How many years of experience do you have programming with Python or Python packages?', choices=[('Less than one year', 'Less than one year'), ('1-2 years', '1-2 years'), ('3-5 years', '3-5 years'), ('6-9 years', '6-9 years'), ('10-19 years', '10-19 years'), ('20 more more years', '20 more more years')]),
        ),
        migrations.AlterField(
            model_name='prequestionnaire',
            name='gender',
            field=models.CharField(max_length=500, null=True, verbose_name='What is your gender?', blank=True),
        ),
        migrations.AlterField(
            model_name='prequestionnaire',
            name='occupation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='What is your primary occupation?', choices=[('Software developer', 'Software developer'), ('Systems administrator', 'Systems administrator'), ('Project manager', 'Project manager'), ('Quality assurance', 'Quality assurance'), ('Graduate student', 'Graduate student'), ('Undergraduate student', 'Undergraduate student'), ('Other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='prequestionnaire',
            name='programming_years',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='How many years of experience do you have programming?', choices=[('Less than one year', 'Less than one year'), ('1-2 years', '1-2 years'), ('3-5 years', '3-5 years'), ('6-9 years', '6-9 years'), ('10-19 years', '10-19 years'), ('20 more more years', '20 more more years')]),
        ),
        migrations.AlterField(
            model_name='prequestionnaire',
            name='python_years',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='How many years of experience do you have programming with Python or Python packages?', choices=[('Less than one year', 'Less than one year'), ('1-2 years', '1-2 years'), ('3-5 years', '3-5 years'), ('6-9 years', '6-9 years'), ('10-19 years', '10-19 years'), ('20 more more years', '20 more more years')]),
        ),
    ]

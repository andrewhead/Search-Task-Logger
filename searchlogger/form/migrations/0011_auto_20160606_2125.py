# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_auto_20160606_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='na_cant_tell',
            field=models.BooleanField(default=False, verbose_name="Can't tell"),
        ),
        migrations.AlterField(
            model_name='postquestionnaire',
            name='important_concern1',
            field=models.CharField(blank=True, choices=[(b'I will be able to find How-To documentation for all the tasks I want to do.', b'I will be able to find How-To documentation for all the tasks I want to do.'), (b'Developers will provide answers to questions I ask as fast as I need them to.', b'Developers will provide answers to questions I ask as fast as I need them to.'), (b'The documentation (e.g., API docs and example code) will reflect the most recent code.', b'The documentation (e.g., API docs and example code) will reflect the most recent code.'), (b'The community will be welcoming when they respond to questions I ask.', b'The community will be welcoming when they respond to questions I ask.'), (b'I can trust the developers of the package to develop reliable, usable software.', b'I can trust the developers of the package to develop reliable, usable software.'), (b'The package was designed for users with my conceptual knowledge and goals.', b'The package was designed for users with my conceptual knowledge and goals.')], max_length=1000, null=True, verbose_name='To me, the most important question from this set when choosing a package is:'),
        ),
        migrations.AlterField(
            model_name='postquestionnaire',
            name='important_concern2',
            field=models.CharField(blank=True, choices=[(b'I will be able to find How-To documentation for all the tasks I want to do.', b'I will be able to find How-To documentation for all the tasks I want to do.'), (b'Developers will provide answers to questions I ask as fast as I need them to.', b'Developers will provide answers to questions I ask as fast as I need them to.'), (b'The documentation (e.g., API docs and example code) will reflect the most recent code.', b'The documentation (e.g., API docs and example code) will reflect the most recent code.'), (b'The community will be welcoming when they respond to questions I ask.', b'The community will be welcoming when they respond to questions I ask.'), (b'I can trust the developers of the package to develop reliable, usable software.', b'I can trust the developers of the package to develop reliable, usable software.'), (b'The package was designed for users with my conceptual knowledge and goals.', b'The package was designed for users with my conceptual knowledge and goals.')], max_length=1000, null=True, verbose_name='The second most important question is:'),
        ),
    ]

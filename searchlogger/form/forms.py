#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django import forms
from django.forms import modelform_factory, Textarea, RadioSelect
from django.utils.safestring import mark_safe

from .models import Question, Prequestionnaire, PackagePair, PackageComparison, Postquestionnaire


logging.basicConfig(level=logging.INFO, format="%(message)s")


# Adapted from code at
# http://stackoverflow.com/questions/1134085/rendering-a-value-as-text-instead-of-field-inside-a-django-form
# This makes it possible to define additional markup as part
# of the model, which is totally bad practice, but makes it
# a lot more adaptable to generate HTML
class PlainTextWidget(forms.Widget):

    def __init__(self, tag, _class=None, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.tag = tag
        self._class = _class

    def render(self, _name, value, attrs):
        result = '<' + self.tag
        if self._class is not None:
            result += (' class=' + self._class)
        result += '>'
        result += mark_safe(value) if not None else '-'
        result += ('</' + self.tag + '>')
        result += "<input type=hidden name='" + _name + "' value='" + value + "'/>"
        return result


QuestionForm = modelform_factory(
    Question,
    exclude=['user', 'question_index', 'created', 'updated'],
    widgets={
        'concern': PlainTextWidget('p', 'question'),
        'strategy': Textarea(),
        'scratch_work': Textarea(),
        'likert_comparison': RadioSelect(),
        'likert_confidence': RadioSelect(),
        'url1_where': Textarea(),
        'url1_what': Textarea(),
        'url1_why': Textarea(),
        'url2_where': Textarea(),
        'url2_what': Textarea(),
        'url2_why': Textarea(),
        'extra_information': Textarea(),
        'comments': Textarea(),
    }
)


PrequestionnaireForm = modelform_factory(
    Prequestionnaire,
    exclude=['user'],
)


PackageComparisonForm = modelform_factory(
    PackageComparison,
    exclude=['user', 'stage'],
    widgets={
        'likert_community': RadioSelect(),
        'likert_documentation': RadioSelect(),
    }
)


PostquestionnaireForm = modelform_factory(
    Postquestionnaire,
    exclude=['user'],
    widgets={
        'change_justification': Textarea(),
    }
)


PackagePairForm = modelform_factory(
    PackagePair,
    exclude=['user']
)

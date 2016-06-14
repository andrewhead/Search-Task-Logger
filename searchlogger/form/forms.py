#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django import forms
from django.forms import modelform_factory, Textarea, RadioSelect
from django.utils.safestring import mark_safe

from .models import Strategy, Question, Prequestionnaire, PackagePair,\
    PackageComparison, Postquestionnaire


logging.basicConfig(level=logging.INFO, format="%(message)s")


# Adapted from code at
# http://stackoverflow.com/questions/1134085/rendering-a-value-as-text-instead-of-field-inside-a-django-form
# This makes it possible to define additional markup as part
# of the model, which is totally bad practice, but makes it
# a lot more adaptable to generate HTML
# Assumption: the value to be shown does not include double-quotation marks.
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
        result += "<input type=hidden name='" + _name + "' value=\"" + value + "\"/>"
        return result


StrategyForm = modelform_factory(
    Strategy,
    fields=[
        'strategy',
    ],
    widgets={
        'strategy': Textarea(),
    }
)


QuestionForm = modelform_factory(
    Question,
    fields=[
        'concern',
        'likert_comparison_evidence',
        'na_likert_comparison_evidence',
        'evidence',
        'likert_confidence',
        'na_likert_confidence',
    ],
    widgets={
        'concern': PlainTextWidget('p', 'question'),
        'likert_comparison_evidence': RadioSelect(),
        'evidence': Textarea(),
        'likert_confidence': RadioSelect(),
    }
)


PrequestionnaireForm = modelform_factory(
    Prequestionnaire,
    exclude=['user'],
)


PackageComparisonForm = modelform_factory(
    PackageComparison,
    fields=[
        'likert_quality',
        'na_likert_quality',
        'likert_preference',
        'na_likert_preference',
    ],
    widgets={
        'likert_quality': RadioSelect(),
        'likert_preference': RadioSelect(),
    }
)


PostquestionnaireForm = modelform_factory(
    Postquestionnaire,
    fields=[
        'likert_perception_change',
        'na_likert_perception_change',
        'concern_rank1',
        'concern_rank2',
        'concern_rank3',
        'concern_rank4',
        'concern_rank5',
        'concern_rank6',
    ],
    widgets={
        'likert_perception_change': RadioSelect(),
    }
)


PackagePairForm = modelform_factory(
    PackagePair,
    exclude=['user']
)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import welcome, prequestionnaire, preinstructions, pretask, precomparison,\
    strategy, task, question, postcomparison, thanks


urlpatterns = [
    url(r'^$', welcome),
    url(r'^welcome/', welcome, name='welcome'),
    url(r'^prequestionnaire/', prequestionnaire, name='prequestionnaire'),
    url(r'^pretask/', pretask, name='pretask'),
    url(r'^preinstructions/', preinstructions, name='preinstructions'),
    url(r'^precomparison/', precomparison, name='precomparison'),
    url(r'^strategy/(?P<question_index>[0-9]+)/$', strategy, name='strategy'),
    url(r'^task/(?P<question_index>[0-9]+)/$', task, name='task'),
    url(r'^question/(?P<question_index>[0-9]+)/$', question, name='question'),
    url(r'^postcomparison/', postcomparison, name='postcomparison'),
    url(r'^thanks/', thanks, name='thanks'),
]

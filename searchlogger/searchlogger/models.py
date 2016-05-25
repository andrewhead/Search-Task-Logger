#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django.db import models


logging.basicConfig(level=logging.INFO, format="%(message)s")


class LocationEvent(models.Model):
    visit_date = models.DateTimeField()
    log_date = models.DateTimeField(auto_now_add=True)
    tab_index = models.IntegerField()
    title = models.CharField(max_length=1024)
    url = models.CharField(max_length=2048)
    event_type = models.CharField(max_length=128)

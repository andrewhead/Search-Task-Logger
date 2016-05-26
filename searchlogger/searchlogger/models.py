#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django.db import models
from django.contrib.auth.models import User


logging.basicConfig(level=logging.INFO, format="%(message)s")


class LocationEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    visit_date = models.DateTimeField(db_index=True)
    log_date = models.DateTimeField(db_index=True, auto_now_add=True)
    tab_index = models.IntegerField()
    title = models.CharField(max_length=1024)
    url = models.CharField(db_index=True, max_length=2048)
    event_type = models.CharField(db_index=True, max_length=128)

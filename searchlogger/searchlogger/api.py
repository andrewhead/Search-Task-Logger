#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from searchlogger.models import LocationEvent


logging.basicConfig(level=logging.INFO, format="%(message)s")


class LocationEventResource(ModelResource):

    class Meta:

        queryset = LocationEvent.objects.all()
        resource_name = 'location_event'

        # Limit operations on this resource to only POST'ing new records
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        detail_allowed_methods = []
        list_allowed_methods = ['post']

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from defaults import *  # noqa
import json


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['.searchlogger.tutorons.com']

# Read in the Postgres database configuration from a file
DATABASE_CONFIG_FILENAME = os.path.join(
    os.path.abspath(os.sep),  # root directory
    'etc', 'django', 'searchlogger', 'database_config.json'
)
with open(DATABASE_CONFIG_FILENAME) as database_config_file:
    database_config = json.load(databse_config_file)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': database_config['name'],
        'USER': database_config['user'],
        'PASSWORD': database_config['password'],
        'HOST': database_config['host'],
        'PORT': database_config['port'],
    }
}

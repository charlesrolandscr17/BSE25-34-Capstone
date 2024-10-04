"""
WSGI config for Group_BSE25_34_Capstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

project_home = '~/Capstone/Group_BSE25-34-Capstone'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'Group_BSE25_34_Capstone.settings')

application = get_wsgi_application()

"""
WSGI config for tikedge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR+'/tikedge/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tikedge.settings.beta")

application = get_wsgi_application()

"""
WSGI config for root project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
sys.path.append('/home/zia/Documents/Codes/Django/sql_api/root')
sys.path.append('/home/zia/Documents/Codes/Django/sql_api')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

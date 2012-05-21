# flake8: noqa
import os
import site
import sys


site.addsitedir('/home/ENV_USER/Envs/VENV_NAME/lib/python2.7/site-packages')
activate_this = os.path.expanduser("~/Envs/VENV_NAME/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))
project = '/home/ENV_USER/webapps/DJANGO_APP_NAME/myproject/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
application = WSGIHandler()

import os, sys
site_user_root_dir = '/home/d/dimastp6/rushytaleshop/public_html'
sys.path.insert(0, site_user_root_dir + '/RusHytale')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'RusHytale.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
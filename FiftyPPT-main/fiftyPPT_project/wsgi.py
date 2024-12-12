"""
WSGI config for fiftyPPT_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
# --------------------------------------------------------------------------
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fiftyPPT_project.settings')

# application = get_wsgi_application()
#
# --------------------------------------------------------------------------
# import os
# import sys

# # Add your project directory to the sys.path
# # project_home = '/home/fiftyppt/fiftyPPT_project'
# # if project_home not in sys.path:
# #     sys.path.append(project_home)

# path='/home/fiftyppt/fiftyPPT_project/fiftyPPT_project'
# if path not in sys.path:
#     sys.path.append(path)

# # Activate your virtualenv
# # activate_this = '/home/fiftyppt/.virtualenvs/fiftyppt/bin/activate_this.py'
# # with open(activate_this) as f:
# #     exec(f.read(), dict(__file__=activate_this))

# # Set the settings module
# os.environ['DJANGO_SETTINGS_MODULE'] = 'fiftyPPT_project.settings'

# # Import Django
# import django
# django.setup()

# # Get the application
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

import os
import sys

activate_this = '/home/fiftyppt/.virtualenvs/fiftyppt/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Add the project directory to the sys.path
path = '/home/fiftyppt/fiftyPPT_project'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'fiftyppt.settings'

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



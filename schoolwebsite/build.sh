#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolwebsite.settings')
django.setup()
from axes.models import AccessAttempt
AccessAttempt.objects.all().delete()
from django.contrib.auth.models import User
if not User.objects.filter(username='hallmark').exists():
    User.objects.create_superuser('hallmark', 'abdulhakeemumar616@gmail.com', 'Academy2026!')
    print('New superuser created!')
else:
    print('User already exists!')
"
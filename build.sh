#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# ✅ 强制创建/更新管理员（无论之前有没有这个用户，密码都会变成环境变量里的那个）
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if not username or not password:
    raise SystemExit('Missing DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD')

u, created = User.objects.get_or_create(username=username, defaults={'email': email, 'is_staff': True, 'is_superuser': True})
if not created and email:
    u.email = email
u.is_staff = True
u.is_superuser = True
u.set_password(password)
u.save()

print('✅ Superuser ready:', username)
"

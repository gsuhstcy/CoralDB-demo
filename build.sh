#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# 自动创建管理员（如果已存在会跳过）
python manage.py createsuperuser --noinput || true

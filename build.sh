#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# 每次部署自动导入 demo 数据（数据库为空时会补齐）
python manage.py loaddata genome/fixtures/demo_seed.json || true

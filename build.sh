#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# ✅ 清空 demo 数据（避免 loaddata 主键/唯一约束冲突）
python manage.py shell -c "from genome.models import SpeciesImage, ResourceFile, Species; SpeciesImage.objects.all().delete(); ResourceFile.objects.all().delete(); Species.objects.all().delete()"

# ✅ 再导入固定 demo 数据（一定成功就会有 3 个）
python manage.py loaddata genome/fixtures/demo_seed.json

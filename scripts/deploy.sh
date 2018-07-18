#!/bin/bash
set -e

./manage.py collectstatic --noinput
# Cheating, making sure that migrate is working
export LAMBDA_TASK_ROOT=/home
./manage.py migrate
# Create an admin when deploying for the first time
echo "from django.contrib.auth.models import User; import os; User.objects.create_superuser('root', 'my@email.com', os.environ.get('DJANGO_ADMIN_PASSWORD','MyPassword')) if len(User.objects.filter(email='my@email.com')) == 0 else print('Admin exists')"|./manage.py shell
# We need the so, Lambda env does not contaon it.
cp ./scripts/_sqlite3.so .
sls deploy
rm _sqlite3.so

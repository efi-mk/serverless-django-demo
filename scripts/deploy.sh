#!/bin/bash

./manage.py collectstatic --noinput
# Cheating, making sure that migrate is working
export LAMBDA_TASK_ROOT=/home
./manage.py migrate
# We need the so, Lambda env does not contaon it.
cp ./scripts/_sqlite3.so .
sls deploy
rm _sqlite3.so

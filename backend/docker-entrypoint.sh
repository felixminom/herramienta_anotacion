#!/usr/bin/env bash

echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 0.5
done

echo "MySQL started"

python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

python3 manage.py run
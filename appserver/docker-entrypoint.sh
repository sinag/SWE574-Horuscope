#!/bin/bash

export DJANGO_SETTINGS_MODULE="root.settings"

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Flush db
# python manage.py flush --no-input

# Create database migrations
echo "Create database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Apply initialization
echo "Apply initialization"
python initialize.py

exec "$@"
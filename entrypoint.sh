#!/bin/sh

PORT=${PORT:-8000}
DEV=${DEBUG:-false}

if [ "$DEV" = "true" ]; then
    MODE="development"
else
    MODE="production"
fi

python manage.py migrate --noinput
python manage.py createsuperuser_from_env

echo "➡ Starting $MODE server on port $PORT"

exec gunicorn --bind 0.0.0.0:$PORT config.wsgi

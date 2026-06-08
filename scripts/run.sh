#!/usr/bin/env sh
set -eu

cd /code

echo "Running database migrations..."
attempt=1
max_attempts="${MIGRATE_MAX_ATTEMPTS:-30}"
while ! python manage.py migrate --noinput; do
    if [ "$attempt" -ge "$max_attempts" ]; then
        echo "Migration step failed after ${max_attempts} attempts."
        exit 1
    fi
    attempt=$((attempt + 1))
    echo "Database not ready yet, retrying in 2 seconds... (${attempt}/${max_attempts})"
    sleep 2
done

if [ -n "${STATIC_ROOT:-}" ]; then
    mkdir -p "$STATIC_ROOT"
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
fi

if [ -n "${DJANGO_SUPERUSER_EMAIL:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
    echo "Ensuring superuser exists from environment..."
    python manage.py create_superuser_from_env
fi

echo "Starting gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers "${GUNICORN_WORKERS:-3}" --timeout "${GUNICORN_TIMEOUT:-120}"

web: ( cd weather2 && gunicorn --workers 2 project.wsgi:app --bind 0.0.0.0:$PORT )
release: python manage.py migrate
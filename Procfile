release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn Tripper.wsgi --log-file -

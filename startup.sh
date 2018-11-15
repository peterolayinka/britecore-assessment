source venv/bin/activate
PWD=root

if [[ $1 == true ]]; then
    python manage.py runserver 0.0.0.0:8000
fi
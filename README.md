Starting:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
6. openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
7. HTTP - python manage.py runserver 0.0.0.0:8000 / HTTPS - python manage.py runserver_plus 0.0.0.0:8000 --cert-file cert.pem --key-file key.pem

To add sample data:
1. runserver on HTTP - python manage.py runserver
2. python add_users.py
3. import data - python manage.py loaddata sample_data.json

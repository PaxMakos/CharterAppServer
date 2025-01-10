Starting:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py loaddata initial_data.json
5. openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
6. HTTP - python manage.py runserver / HTTPS - python manage.py runserver_plus --cert-file cert.pem --key-file key.pem

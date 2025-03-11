# CharterAppServer

CharterAppServer is a server-side application designed to manage and serve charter-related data. It utilizes Python and Django to provide a robust and scalable backend solution. It provides data for Android CharterApp. Link to the project: https://github.com/Wojciech-Krol/CharterApp

## Features

- **User Management**: Create and manage user accounts with administrative privileges.
- **Data Handling**: Import and manage sample data for charters.
- **Secure Connections**: Support for HTTPS using SSL certificates.

## Getting Started

Follow these steps to set up and run the CharterAppServer on your local machine.

### Setup

1. **Apply migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the admin account.

3. **Generate SSL certificates (for HTTPS)**:

   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```

   Provide the necessary information when prompted.

### Running the Server

- **For HTTP**:

  ```bash
  python manage.py runserver 0.0.0.0:8000
  ```

- **For HTTPS**:

  ```bash
  python manage.py runserver_plus 0.0.0.0:8000 --cert-file cert.pem --key-file key.pem
  ```

  Note: Ensure you have the `django-extensions` package installed to use `runserver_plus`.

### Adding Sample Data

1. **Start the server** (ensure it's running on HTTP):

   ```bash
   python manage.py runserver
   ```

2. **Add users**:

   ```bash
   python add_users.py
   ```

3. **Import sample data**:

   ```bash
   python manage.py loaddata sample_data.json
   ```

## Android App

This server provides data for Android CharterApp. Link to the project: https://github.com/Wojciech-Krol/CharterApp

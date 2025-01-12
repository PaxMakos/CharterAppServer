import requests

# URL of the registration endpoint
url = "http://127.0.0.1:8000/db/register/"

# User data
users = [
    {
        "username": "user1",
        "password": "password1",
        "email": "user1@example.com"
    },
    {
        "username": "user2",
        "password": "password2",
        "email": "user2@example.com"
    },
    {
        "username": "user3",
        "password": "password3",
        "email": "user3@example.com"
    }
]

# Send POST requests to register users
for user in users:
    response = requests.post(url, data=user)
    if response.status_code == 200:
        print(f"User {user['username']} registered successfully.")
    else:
        print(f"Failed to register user {user['username']}. Response: {response.text}")
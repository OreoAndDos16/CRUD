# auth.py

USER_CREDENTIALS = {
    "admin": "admin123"
}

def validate_login(username, password):
    return USER_CREDENTIALS.get(username) == password
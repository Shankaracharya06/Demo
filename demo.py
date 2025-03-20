import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def generate_token():
    payload = {
        "user": "admin",
        "exp": datetime.now() + timedelta(hours=1)  # Token expires in 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(generate_token()) 
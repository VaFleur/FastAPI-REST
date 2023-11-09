import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from src.config import SECRET_AUTH

SECRET_KEY = SECRET_AUTH
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=30)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None

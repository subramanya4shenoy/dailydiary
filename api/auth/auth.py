from datetime import datetime, timedelta
import os
from passlib.context import CryptContext
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY=os.getenv("SECRET_KEY")
ALGO="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=36000

def hash_password(password: str) -> str:   
    return pwd_context.hash(password)

def verify_password(plain_password:str, password: str) -> bool:
    return pwd_context.verify(plain_password, password)

def create_access_token(data: dict, expirationtime: timedelta|None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expirationtime or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)
    return encoded_jwt
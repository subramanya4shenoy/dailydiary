from datetime import datetime, timedelta
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from db.database import get_db
from sqlalchemy.orm import Session
from models.user import User



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY=os.getenv("SECRET_KEY")
ALGO="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

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

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGO)
        user = db.query(User).filter(User.id == payload["sub"]).first()
        return user
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
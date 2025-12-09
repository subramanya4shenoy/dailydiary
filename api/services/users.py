
from auth.auth import hash_password, verify_password
from models.user import User
from schemas.users import UserLogin, UserPreference, UserSignup
from sqlalchemy.orm import Session


def is_existing_user(username: str, db: Session) -> bool:
    return db.query(User).filter(User.email == username).first() is not None

def signup_user(user: UserSignup, db: Session):
    hashed_password = hash_password(user.password)
    new_user = User(email=user.user_email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email,
        "created_at": new_user.created_at,
        "last_accessed": new_user.last_accessed
    }

def get_user_with_email(email:str, db):
    user = db.query(User).filter(User.email == email).first()
    return user


def login_user(email: str, password: str, db: Session) -> UserPreference:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    
    if not verify_password(password, user.password_hash):
        return False
    
    return user

    

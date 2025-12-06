
from models.user import User
from schemas.users import UserSignup
from sqlalchemy.orm import Session

def signup_user(user: UserSignup, db: Session):
    new_user = User(email = user.user_email, password_hash = user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
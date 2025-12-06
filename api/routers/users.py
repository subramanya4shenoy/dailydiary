from fastapi import APIRouter, Depends, status
from db.database import get_db
from schemas.users import UserOut, UserSignup
from services.users import signup_user
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    new_user = signup_user(user, db)
    return {'email': new_user.email, 'password': new_user.password_hash}


@router.post("/login")
def login():
    return { 'login_status': 'ok'}
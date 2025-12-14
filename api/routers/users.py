from fastapi import APIRouter, Depends, Form, HTTPException, status
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from auth.auth import create_access_token
from db.database import get_db
from schemas.users import UserLogin, UserPreference, UserSignup
from services.users import is_existing_user, login_user, signup_user
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/signup", response_model=UserPreference, status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    # check if user exists
    if is_existing_user(user.user_email, db):
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, 
                            detail={
                                'code': 400, 
                                "msg":"user already  exists"
                                }
                            )
    # create new user
    new_user = signup_user(user, db)
    # if creationfails
    if new_user is None:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, 
                            detail={
                                "code": "403", 
                                "msg": "Signup Failed badlY!"
                                }
                            )
    # on scuccessful creation of user
    if new_user:
        return {
            'email': new_user['email'], 
            'token': create_access_token({"sub": new_user["id"]})
            }


@router.post("/login", response_model=UserPreference, status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    if not is_existing_user(form_data.username, db):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="user not found")
    
    valid_user = login_user(form_data.username, form_data.password, db)
    
    if not valid_user:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Forbidden")
    
    return { 'email': valid_user.email,  'token': create_access_token({"sub": str(valid_user.id)})}


from pydantic import BaseModel, EmailStr
class UserSignup(BaseModel):
    user_email: EmailStr
    password: str

class UserLogin(BaseModel):
    user_email: str
    password: str

class UserPreference(BaseModel):
    email: str
    token: str

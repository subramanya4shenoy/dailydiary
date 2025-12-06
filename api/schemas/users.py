

from pydantic import BaseModel, EmailStr
class UserSignup(BaseModel):
    user_email: str
    password: str

class UserLogin(BaseModel):
    user_email: str
    password: str

class UserOut(BaseModel):
    email: str
    password: str

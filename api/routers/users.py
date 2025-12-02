from fastapi import APIRouter


router = APIRouter()

@router.post("/signup")
def signup():
    return { 'signup_status': 'ok'}


@router.post("/login")
def signup():
    return { 'login_status': 'ok'}
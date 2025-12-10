from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from auth.auth import get_current_user
from schemas.diary import Page

router = APIRouter()

@router.get("/diary/{diary_page}")
def read_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.post("/diary")
def add_diary_page(page: Page, current_user = Depends(get_current_user)):
    return { "status": "ok", "requested": page, "current_user": current_user}

@router.put("/diary/{diary_page}")
def update_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.delete("/diary/{diary_page}")
def remove_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}
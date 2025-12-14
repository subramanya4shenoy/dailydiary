from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from auth.auth import get_current_user
from schemas.diary import Page
from services.diary import post_diary_page, delete_diary_page, get_diary_page, put_diary_page, get_all_diary_pages
from typing import List
router = APIRouter()



@router.get("/diary/{diary_page}")
def fetch_diary_page(diary_page: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """ Get specific diary page by id """
    page = get_diary_page(diary_page, db, current_user)
    if page is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Page not found")
    return { "status": "ok", "requested": page}



@router.post("/diary")
def create_diary_page(page: Page, 
                db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
    """ Create a new diary page """
    new_diary_page = post_diary_page(page, db, current_user)
    if not new_diary_page:
        raise HTTPException(status_code=status.HTTP_400_BAD_Request, detail="Failed to create diary page")
    return { "status": "ok", "details": new_diary_page}



@router.put("/diary/{diary_page}")
def update_diary_page(diary_page: str, page: Page, db: Session = Depends(get_db), current_user = Depends(get_current_user)): 
    """ Update a specific diary page by id """
    page = put_diary_page(diary_page, page, db, current_user)
    if page is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Page not found")
    return { "status": "ok", "requested": page}



@router.delete("/diary/{diary_page}")
def remove_diary_page(diary_page: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    page = delete_diary_page(diary_page, db, current_user)
    if page is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Page not found")
    return { "status": "ok", "requested": page}

@router.get("/diary", response_model=List[Page])
def fetch_all_diary_pages(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    pages = get_all_diary_pages(db, current_user)
    return pages or []
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from auth.auth import get_current_user
from schemas.diary import Page
from services.diary import create_diary, read_diary_page
router = APIRouter()

@router.get("/diary/{diary_page}")
def get_diary_page(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    """
    Read a diary page from the database
    Args:
        diary_page: str
    Returns:
        diary_page: Diary
    """
    page = read_diary_page(diary_page, db, current_user)
    if page is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Page not found")
    return { "status": "ok", "requested": page}

@router.post("/diary")
def post_diary_page(page: Page, 
                db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
    """
    Add a new diary page to the database    
    Args:
        page: Page
        db: Session
        current_user: User
    Returns:
        new_diary_page: Diary
    """
    new_diary_page = create_diary(page, db, current_user)
    if not new_diary_page:
        raise HTTPException(status_code=status.HTTP_400_BAD_Request, detail="Failed to create diary page")
    return { "status": "ok", "details": new_diary_page}

@router.put("/diary/{diary_page}")
def update_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.delete("/diary/{diary_page}")
def remove_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}
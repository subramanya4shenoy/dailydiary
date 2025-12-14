from sqlalchemy.orm import Session
from schemas.diary import Page
from models.user import User
from models.diary import Diary
from datetime import datetime

def post_diary_page(page: Page, db: Session, current_user: User):
    diary_id = str(datetime.now().strftime("%Y%m%d"))
    old_page = db.query(Diary).filter(Diary.diary_id == diary_id, Diary.user_id == current_user.id).first()
    if old_page is not None:
        put_diary_page(diary_id, page, db, current_user)
        return old_page
    
    new_diary_page = Diary(
        title=page.title,
        body=page.body,
        user_id=current_user.id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        diary_id=diary_id,
        tags= []
    )
    db.add(new_diary_page)
    db.commit()
    db.refresh(new_diary_page)
    return new_diary_page


def get_diary_page(diary_id: str, db: Session, current_user: User):
    page = db.query(Diary).filter(Diary.diary_id == diary_id, Diary.user_id == current_user.id).first()
    return page

def put_diary_page(diary_id: str, page: Page, db: Session, current_user: User):
    old_page = db.query(Diary).filter(Diary.diary_id == diary_id, Diary.user_id == current_user.id).first()
    print("page =>", old_page)
    if old_page is None:
        return None
    old_page.title = page.title
    old_page.body = page.body
    old_page.updated_at = datetime.now()
    old_page.diary_id = diary_id
    db.commit()
    db.refresh(old_page)
    return old_page

def delete_diary_page(diary_id: str, db: Session, current_user: User):
    old_page = db.query(Diary).filter(Diary.diary_id == diary_id, Diary.user_id == current_user.id).first()
    if old_page is None:
        return None
    db.delete(old_page)
    db.commit()
    return old_page

def get_all_diary_pages(db: Session, current_user: User):
    pages = db.query(Diary).filter(Diary.user_id == current_user.id).all()
    if pages is None:
        return []
    return [Page(title=page.title, body=page.body, diary_id=page.diary_id) for page in pages]
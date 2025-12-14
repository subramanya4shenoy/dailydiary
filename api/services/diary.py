from sqlalchemy.orm import Session
from schemas.diary import Page
from models.user import User
from models.diary import Diary
from datetime import datetime

def create_diary(page: Page, db: Session, current_user: User):
    new_diary_page = Diary(
        title=page.title,
        body=page.body,
        user_id=current_user.id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        diary_id=str(datetime.now().strftime("%Y%m%d")),
        tags= []
    )
    db.add(new_diary_page)
    db.commit()
    db.refresh(new_diary_page)
    return new_diary_page


def read_diary_page(diary_id: str, db: Session):
    page = db.query(Diary).filter(Diary.diary_id == diary_id).first()
    return page
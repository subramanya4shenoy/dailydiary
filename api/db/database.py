import os
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo= False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connetion():
    """Simple select 1 to confirm DB is alive or not"""
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

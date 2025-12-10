from db.database import Base
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import (Integer, String, Text, DateTime)

class Diary(Base):
    __tablename__ = "diary"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String[255], nullable=False)
    body: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    mood: Mapped[str] = mapped_column(String[255], nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    tags: Mapped[str] = mapped_column(Text, nullable=True)
    diary_id: Mapped[str] = mapped_column(Text, nullable=False)

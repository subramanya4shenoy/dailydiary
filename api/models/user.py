from datetime import datetime
from email.policy import default
from typing import Optional
from db.database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (Integer, String, DateTime)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String[255], unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String[255], nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    last_accessed: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    info: Mapped[Optional["UserInfo"]] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")


class UserInfo(Base):
    __tablename__ = 'user_info'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    assumed_age: Mapped[int] = mapped_column(Integer, nullable=True)
    assumed_gender: Mapped[int] = mapped_column(Integer, nullable=True)

    user: Mapped["User"] = relationship(back_populates="info")
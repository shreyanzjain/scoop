from src.database import Base
from sqlalchemy import Column, String, Date, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(18), unique=True)
    password = Column(String(64))
    date_registered = Column(Date, default=datetime.utcnow)

    scores = relationship("UserScores", back_populates="user")
    resume = relationship("UserResume", back_populates="user")

class UserScores(Base):

    __tablename__ = "user_scores"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String)
    company = Column(String)
    score = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="scores")

class UserResume(Base):

    __tablename__ = "user_resumes"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="resume")
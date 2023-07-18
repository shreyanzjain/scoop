from src.database import Base
from sqlalchemy import Column, String, Date, Integer, Float
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(18), unique=True)
    password = Column(String(64))
    resume_path = Column(String)
    date_registered = Column(Date, default=datetime.utcnow)

class UserScores(Base):

    __tablename__ = "user_scores"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String)
    company = Column(String)
    score = Column(Float)
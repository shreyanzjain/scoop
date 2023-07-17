from src.database import Base
from sqlalchemy import Column, String, Date, Integer
from datetime import datetime

class User(Base):

    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(18))
    password = Column(String(64))
    date_registered = Column(Date, default=datetime.utcnow)
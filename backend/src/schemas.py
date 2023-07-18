from pydantic import BaseModel
from datetime import datetime

# User
class UserBase(BaseModel):

    username: str

class UserCreate(UserBase):

    password: str

class UserLogin(UserCreate):

    pass

class User(UserBase):

    id: int
    date_registered: datetime

    class Config:
        from_attributes = True

class UserScoresBase(BaseModel):
    pass

# User Scores
class UserScoresCreate(UserScoresBase):
    job_title: str
    company: str
    score: float

class UserScores(UserScoresBase):
    id: int
    user_id: int
    job_title: str
    company: str
    score: float

    class Config:
        from_attributes = True
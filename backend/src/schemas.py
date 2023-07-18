from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):

    username: str

class UserCreate(UserBase):

    password: str

class UserLogin(UserCreate):

    pass

class UserResumeUpload(UserBase):

    resume_path: str

class User(UserBase):

    id: int
    date_registered: datetime

    class Config:
        from_attributes = True

class UserScoresBase(BaseModel):
    pass

class UserScoresCreate(UserScoresBase):
    job_title: str
    company: str
    score: float

class UserScores(UserScoresCreate):
    id: int

    class Config:
        from_attributes = True
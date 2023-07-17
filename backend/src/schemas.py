from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):

    username: str

class UserCreate(UserBase):

    password: str

class User(UserBase):

    id: int
    date_registered: datetime

    class Config:
        from_attributes = True
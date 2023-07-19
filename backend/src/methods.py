from sqlalchemy.orm import Session
from src import models, schemas
import bcrypt
from fastapi import HTTPException

def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = bcrypt.hashpw(bytes(user.password, encoding="utf-8"), 
                                    bcrypt.gensalt()).decode("utf-8")
    new_user = models.User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(user: schemas.UserLogin, db: Session):
    tmp_user = db.query(models.User).filter(models.User.username == user.username).first()
    if tmp_user:
        hashed_password = tmp_user.password
        print(len(hashed_password))
        is_valid = bcrypt.checkpw(bytes(user.password, "utf-8"), 
                                  bytes(hashed_password, "utf-8"))
        if is_valid:
            # placeholder
            return {"Valid": "Password"}
        else:
            # placeholder
            return {"Invalid": "Password"}
    else:
        raise HTTPException(400, 'User not found.')
    
def add_score(username: str, create_score: schemas.UserScoresCreate, db: Session):
    new_score = models.UserScores(**create_score.model_dump(), username=username)
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    return new_score
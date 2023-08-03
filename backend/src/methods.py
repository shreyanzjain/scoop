from sqlalchemy.orm import Session
from src import models, schemas
import bcrypt
from fastapi import HTTPException
import globals
import docx2txt as dxt
from rake_nltk import Rake


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

def extract_keywords_from_docx(username: str, db: Session):
    file_location = globals.get_file_path_docx(username)
    resume_text = dxt.process(file_location)
    r = Rake()
    r.extract_keywords_from_text(resume_text)
    keywords = set()
    for i in r.frequency_dist:
        keywords.add(i)
    return keywords

def extract_keywords_from_job_desc_text(username: str, text: str, db: Session):
    r = Rake()
    r.extract_keywords_from_text(text=text)
    keywords = set()
    for i in r.frequency_dist:
        keywords.add(i)
    return keywords
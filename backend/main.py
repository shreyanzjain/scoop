from fastapi import FastAPI, HTTPException, Request, Depends
from typing import List
from typing_extensions import Annotated
from src.database import SessionLocal, engine
from sqlalchemy.orm import Session
from src import models, schemas, methods

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# placeholder logged in user
curr_user_id: int = 1

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/user/create", response_model=schemas.User)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return methods.create_user(user, db)

@app.post("/user/sessions")
def auth_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return methods.authenticate_user(user, db)

@app.post("/user/{user_id}/score", response_model=schemas.UserScores)
def add_score(user_id: int, create_score: schemas.UserScoresCreate, db: Session = Depends(get_db)):
    return methods.add_score(user_id, create_score, db)

@app.get("/user/score", response_model=List[schemas.UserScores])
def get_user_posts(db: Session = Depends(get_db)):
    return db.query(models.UserScores).filter(models.UserScores.user_id == curr_user_id).all()
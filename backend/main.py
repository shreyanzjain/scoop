from fastapi import FastAPI, HTTPException, Request, Depends
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

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/user/create", response_model=schemas.User)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return methods.create_user(user, db)

@app.post("/user/sessions")
def auth_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return methods.authenticate_user(user, db)
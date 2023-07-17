from fastapi import FastAPI, HTTPException, Request
from src.database import SessionLocal, engine
from sqlalchemy.orm import Session
from src import models, schemas

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
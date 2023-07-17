from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
from fastapi import FastAPI

from app.database.db import Base, engine
from app.models.course import Course

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DevOpsMart API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to DevOpsMart"}